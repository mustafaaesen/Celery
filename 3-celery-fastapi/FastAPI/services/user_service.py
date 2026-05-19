#kurallar ve kararlar buradadır backendin beynidir
#routesta öağırılan fonksiyonlar ve çıktıları yer alır

from celery_worker.tasks.activity_tasks import log_activity
#activity sevsinin import edilemsi yapılanalarda aktivite kaydı için
#ör kullanıcı kayıt tarihi yapılma tarihi etkisinin kadı gibi
from sqlalchemy.orm import Session
from models.user_models import User
from schemas.user_schemas import UserCreate
from services.redis_service import get_cache, set_cache,delete_cache

from sqlalchemy.exc import IntegrityError

def create_user(db: Session, user_data: UserCreate):

    if len(user_data.username)<3:

        raise ValueError("Username must be at least 3 characters")

    user=User(
        username=user_data.username,
        email=user_data.email
    )
    
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")

    db.refresh(user)

    #log activity artık senkron değil asnekron olacak celery sayesinde
    
    log_activity.delay(user.id,"user_created")
    
    
    #cache invalidate
    
    #yeni kulalnıcı eklendiği için liste artık geçersiz silinmesi gereklidir
    #sonraki cache miss te zaten gelir
    
    delete_cache("users:all")

    return user




#kuallnıcı ooluşturmak için routes ta çapğırlır şartkarı sağlarsa yeni kullanıcı sağlamazsa hata mesajını döner

def list_users(db: Session):

    cache_key= "users:all"
    
    #cache check
    
    cached_user=get_cache(cache_key)
    
    if cached_user: #rediste olma durumu cache hit
        print("CACHE HIT")
        return cached_user
    
    #rediste yoksa miss tir db den alır
    
    print("CACHE")
    
    users=db.query(User).all()
    
    #SQL Alchemmy objesini dicte çevirme işlemi
    
    users_data=[
        
        {"id": u.id, "username": u.username, "email": u.email}
        
        for u in users
    ]
    
    #CACHE e yazma
    
    set_cache(cache_key,users_data, ttl=60)
    
    return users_data

    
     #routes ta tüm listeleme route ında çağırlır tüm kayıtları döner

def get_user_by_id(db: Session, user_id: int):

    #id ye göre kullanıcı edinme
    #eğer cache te varsa dönerse yoksa db den döner
    #cache key oluşturulur->kontrol edilir->varsa döner->yoksa db den döner
    
    #cache key
    
    cache_key=f"user:{user_id}"
    
    #key ile cache kontrolü
    
    cached_user=get_cache(cache_key)
    
    if cached_user:
        print("CACHE HIT (user)")#cache te olması durumu 
        
        return cached_user
    
    #aksi halde misstir db den döner
    
    print("CACHE MISS (user)")
    
    
    
    user= db.query(User).filter(User.id==user_id).first()
    #db den sorgu
    
    if not user:
        #kullanıcı bulunamadıysa
        
        return None
    
    #serializaiton
    #sqlachemmy den dönen sorgunun jsona çevirilebilir hale getirme
    
    user_data={
        "id": user.id,
        "username":user.username,
        "email":user.email
    }    
    
    
    #Cache set
    
    set_cache(cache_key,user_data,ttl=60)
    
    return user_data
    
 
  #id sine göre kullanıcı arayan kısım

def delete_user(db:Session ,user_id : int):

    #delete tarafında br fark var silinmeden response dönülmez
    
    #silme işlemi o yüzden sync olmalı log kısmı celery olabilir
    
    

    user=db.query(User).filter(User.id == user_id).first()
    #db den kullanıcı çekimi

    if not user:

        return False #kullanıcı yoksa flase döner
    
    db.delete(user)
    db.commit()

    #celery eklenebiilir async olarak
    log_activity.delay(user.id,"user_deleted")
    #kullanıcı listesi değişti artık geçersiz
    
    delete_cache("users:all")

    return user





