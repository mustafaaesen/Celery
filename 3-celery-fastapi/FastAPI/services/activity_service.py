from sqlalchemy.orm import Session
from models.activity_models import UserActivity



def log_activity(db: Session, user_id:int, action: str):

    activity=UserActivity(
        user_id=user_id,
        action=action
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)


    return activity   #yan etikleri kaydını yapacak servis

def list_activities(db: Session):
    return db.query(UserActivity).order_by(UserActivity.timestamp.desc()).all()
#tüm aktiviteleri listeler