from sqlalchemy import Column,Integer,String
from database import Base


#kullanıcı için veritabanı yapısının kurulması model ile

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(50), nullable=False)
    email=Column(String(250),unique=True,nullable=False)

#srvice katmanına bağlanılarak tablolar oluşturulur

