#user activity yapılan ana işlerin yan etkileridir sistemde kullanıcı oluştruuldu ,silindi,kaydedildi,listelem yapıldı
#ileride login logout işlemleri gibi

#activity verisnin şeklini kaydeder veriler ve tipleri

from pydantic import BaseModel
from datetime import datetime

class UserActivity(BaseModel):
    user_id:int
    action: str
    timestamp:datetime

    class Config:
        from_attributes = True #sqlalchey obejesini pydantice çevirir