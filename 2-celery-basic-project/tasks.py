#uzun süren işlemi uygualmadan ayırarak hız kazanmanin amaçlandığı basit celery projesi

#kullanıcı işşem başlatır->işlem hemen yapılamz->celery workera gider->worker da yapılır

#celery de hazır olan özelliklerden bazıları da burada test edilmiştir

#1)RETRY->Task hata alırsa otomatik olarak tekrar başlatılır 
#          tasks.py içinde task decoratorda yzılır

#2)ERROR HANDLING->Task hata verdiğinde sistemin çökememsini sağlar sadece ilgili yer etkleniir
            #tasks.py içinde raise retry meanizması ile tanımlanır
            
#3)CONCURRENCY->Aynı anda birden azla task çalışır
            #tasks.py içinde time_limit olarak
            
#4)TASK STATE -> Durum takibi(Pending started success)
            #tasks.py backend ile + app.py de tanımlanır
            
            

from celery import Celery
import time 
import random 


#celery uygulaması oluşturma

celery=Celery("tasks",
              broker="redis://localhost:6379/0", #redis task queue işle tutulur
              backend="redis://localhost:6379/0" #task state/result tutulur
              
              )
#uygulama keyi ve broker olan redis bağlantısı ile celery uygulaması oluşturuldu


#celery task tanımı
@celery.task(
    bind=True, #sel erişimi sağlar retry gibi işlemler için gereklidir decorator mantığı
    
    autoretry_for=(Exception,),# exception durumudna otomatik retry için 
    retry_kwargs={
        "max_retries":3,# maximum deneme sanyısı tanımı
        "countdown":2 #iki retry arasuında beklenecek süre
    }
    
    )#asenkron task


def long_task(self, x,y):#taskin çalıştıracağı fonksiyon
    
   
    
    print("task başlatıldı...")
    
    
    time.sleep(5)#uzun süren iş simülasyonu
    
    #retry test etmek için radnom hata üretimi
    
    if random.choice([True,False]):
        print("Hata oluştu! -> Retry tetikleniyor...")
        
        raise Exception("Radnom Fail...")#celery yakalar ve retry başlatır
    
    result=x +y
    
    print("task bitti: ",result)
    
    return result

