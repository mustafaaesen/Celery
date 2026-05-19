#kulalnıcı kaydı yapıldıktan sorna log activities altında 
#kullanıcnın hareketleri kaydediliyordu. Bunu db ye api den sorna keydetmekrequest bekletir.
#yavaşlatma oluşturur.

#celery burada bu işi ana uygulamadan koparıp arkaplanda yaparak paralellik ve hız kazandıracak

#bu aşamadan sonra service tarafı doğrudan db ye yazmak yerine iş üretecek  worker db ye yazacak

from celery import Celery 


#celery app oluşturma bunun üzerinden workerlar için konfigürasyon yapılır

celery=Celery(
    "fastapi-app",
    #uygulama adı
    
    broker="redis://redis-service:6379/0",
    #taskalrın yürütüleceği broker redis
    
    backend="redis://redis-service:6379/0"
    #backend task sunucu state bilgisi tutulur
    
)
import celery_worker.tasks.activity_tasks
