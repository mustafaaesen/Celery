from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime
from database import Base

#yan etkilrin tutulan kayıtları için db modeli

class UserActivity(Base):

    __tablename__ ="user_activities"

    id =Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    action=Column(String(100),nullable=False)
    timestamp=Column(DateTime, default=datetime.utcnow)


#service katmanına bağlanıalrak tablolar oluşturulur