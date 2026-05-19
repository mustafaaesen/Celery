#kullanıcı yönetimi apı'yı

#kullanıcınların crud işlemlerinin olduğu aktiviteleri ve hataları içeren
#FastAPI senaryosu çalışılmıştır.


#main py fastapı uygulmasını ayağı kaldırır ve routeları bağlar yönetim tarafıdır.
from models.user_models import Base
from database import engine
from fastapi import FastAPI

import models.user_models
import models.activity_models
from routes.user_routes import router as user_router
from routes.activity_routes import router as activity_router
Base.metadata.create_all(bind=engine)
app=FastAPI(title="User Managemnet API")
Base.metadata.create_all(bind=engine)

app.include_router(user_router,prefix="/users",tags=["users"])
#kullanıcı ile ilgili tüm endpointleri uygulmaya dahil eder
app.include_router(activity_router, tags=["Activities"])
#activity route ının eklenmesi 



#------------------- DB Bağlantısı-----------------------

from sqlalchemy import text
from database import engine


@app.on_event("startup")
def test_db_connection():

    try:
        with engine.connect() as conn:

            conn.execute(text("SELECT 1"))
        print("PostgreSQL Bağlantısı Başarılı")
    
    except Exception as e:
        print("PostgreSQL Bapaltnısı Hatası",e)


@app.get("/health/db")
def db_health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    
    return  {"status":"db ok"}