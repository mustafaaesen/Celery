#docker tarafında yağı kaldırılan posrtgresql sevisi ile fastapı uygulamasının bağlantılarının gerçekleşştirildiği yerdir

from sqlalchemy import create_engine #postgresql bağlantısı için
from sqlalchemy.orm import sessionmaker,declarative_base #session oturumu ve orm model yapısı
import os #.env den değişkenleri okumak için kullanılacak

# veritabanı gibi değişknelrin bilgilerini soft code şekilde yazıp kullandırmak için açıldı
DATABASE_URL= os.getenv("DATABASE_URL")


engine=create_engine(
    DATABASE_URL,
    pool_pre_ping=True # db restrart olması durumunda bağlantı kopmaması için best practice
)

SessionLocal=sessionmaker(#db ile konuşmak için session
    autocommit=False, # otomatik commit kapalı transictionn kotnrolü için
    autoflush=False, #performan için kapalı
    bind=engine 

)

Base=declarative_base()  #db için modeller üzerine yazılır

def get_db():
    
    db=SessionLocal() # veritabnı bağlantısı oluşturma

    try:     #istek gelir db başlar istek gelir kapanır hafıza verimi için tercih edilir hata durumunda db döner
        yield db

    finally:
        db.close()