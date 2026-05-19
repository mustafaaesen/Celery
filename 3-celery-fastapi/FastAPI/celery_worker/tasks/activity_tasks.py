#celery_app teki uuygulama dahil edilir

from celery_worker.celery_app import celery

from database import SessionLocal #db bağlantısı için

from models.user_models import User
from models.activity_models import UserActivity #model 

@celery.task
def log_activity(user_id,action):
    
    db=SessionLocal()
    #workerlar için db bağlantısı tanımı her biri kendine ayrı açar
    
    #ORM işlemi ile activity nesnesi tanımı
    
    activity=UserActivity(
        user_id=user_id,
        action=action
    )
    
    
    
    #db ye yazma
    db.add(activity)
    
    db.commit()#değişiklikleri kadyedilmesi
    
    db.close()#bağlantı sonlandırma
    
    return "activity logged"