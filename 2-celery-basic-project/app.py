#tasklarin çalıştırlacağı app dosyası genelde proje dosyaları olacaktır

from tasks import long_task

#task gönderme

result=long_task.delay(3,5)
#delay fonksiyonu  açlıştırmaz 
#task'ı redis queue'ya gönderir worker çalıştırır


print("Task Kuyruğa Gönderildi...")


#Task ID takip için

print("Task ID: ",result.id)
#her task unique id alır

#task durumu kontrolü

print("Task Satate:",result.status)
#olabilecek durumlar
#PENDING->Queue'da bekliyor
#STARTED-> Worker aldı
#RETRY-> Tekrar deniyor
#SUCCESS-> Tamamlandı
#FAILURE->Çöktü

