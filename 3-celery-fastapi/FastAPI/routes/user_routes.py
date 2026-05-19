#API Katmanı (Controlelr)
#HTTP ile ilgilenir rquest alır responde döner status code belirler
#iş kuralı yazmaz veri tutmaz

from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_schemas import UserCreate,UserResponse
from services.user_service import create_user,list_users,get_user_by_id,delete_user

router=APIRouter()

#user endpointi oluşturma kısmı repsonse döner kullanıcı requestini alıp başarılıysa defaultu 201 dir aksi halde hata döner
@router.post("/",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate,db: Session=Depends(get_db)):
    try:

        return create_user(db,user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@router.get("/",response_model=list[UserResponse])# get metodu ile kullanıcı listeleme tamamı için response 
def list_users_endpoint(db: Session=Depends(get_db)):
    return list_users(db)#service fonksiyonu çalğırma


@router.get("/{user_id}",response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session=Depends(get_db)):
    user=get_user_by_id(user_id) #kullanıcı id sine göre listeleme için route
    #id ye göre arayan servise gönderip kullanıcı bilgisi alma

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    return user  #hata varsa öesajı döner yoksa kullanıcı vardır onu döner


@router.delete("/{user_id}")
def delete_user_endpoint(user_id : int, db: Session=Depends(get_db)):

    if not delete_user(db, user_id): #delete userdan olumsuz sonuç gelirse
        raise HTTPException(status_code=404,detail="User Not Found")
    
    return {"message":"User Deleted"}

