#veri sözleşmeleri ve apı ye giriş çıkış yapan verilerin şeklini belirler
#validation burada olur
#alacağı ve geri döneceği verileri ve tiplerini barındırır

from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel): #requet model
    username:str
    email:EmailStr

class UserResponse(BaseModel):

    id: int
    username: str
    email: str
