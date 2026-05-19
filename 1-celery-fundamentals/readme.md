# Celery Fundamentals



## Celery Nedir

Celery, Python uygulamalarında uzun süren işlemleri ana uygulamadan ayırarak arka planda çalıştırmayı sağlayan bir task queue sistemidir. Uygulamanın ana akışını (request-response) bloklamadan işlerin başka bir process tarafından yürütülmesini sağlar.

Celery, tek başına çalışan bir sistem değildir. Bir mesaj kuyruğu (broker) ile birlikte çalışır. Bu broker genellikle Redis veya RabbitMQ olur.

## Temel Problem

Bir API içerisinde bazı işlemler anlık olarak tamamlanamayacak kadar uzun sürebilir. Bu tür işlemler:

- kullanıcıyı bekletir
- response süresini uzatır
- sistem performansını düşürür

Bu durumda işlem doğrudan request içerisinde çalıştırıldığında sistem verimsiz hale gelir.

Celery bu problemi şu şekilde çözer:

- işlemi ana uygulamadan ayırır
- bir kuyruğa gönderir
- ayrı bir worker process tarafından çalıştırır

## Çalışma Mantığı

Celery’nin çalışma mantığı üç ana bileşen üzerine kuruludur:

### Producer (Uygulama)

Uygulama, yapılacak işi üretir ve kuyruğa gönderir. Bu aşamada iş çalıştırılmaz, sadece iletilir.

### Broker (Mesaj Kuyruğu)

Gönderilen işler burada tutulur. Broker, işleri sıraya koyar ve worker’ların erişebileceği şekilde saklar.

### Worker (Çalıştırıcı)

Worker, kuyruğu sürekli dinler. Yeni bir iş geldiğinde alır ve çalıştırır. İş tamamlandıktan sonra sonuç oluşturulabilir veya sistemden çıkar.

Bu yapı sayesinde uygulama ile işin çalıştırıldığı ortam birbirinden ayrılmış olur.

## Celery’nin Sağladığı Temel Özellikler

Celery, manuel olarak yazılması gereken birçok altyapıyı hazır olarak sağlar:

- **Task Queue Yönetimi:** Gelen işler otomatik olarak sıraya alınır ve düzenli şekilde işlenir.
- **Worker Yönetimi:** Birden fazla worker process çalıştırılarak paralel işlem yapılabilir.
- **Concurrency:** Aynı anda birden fazla iş yürütülebilir.
- **Retry Mekanizması:** Başarısız olan işler belirli kurallara göre tekrar denenebilir.
- **Hata Yönetimi:** Bir işin hata vermesi tüm sistemi etkilemez, izole şekilde yönetilir.
- **Timeout Kontrolü:** Belirli süreden uzun süren işler durdurulabilir.
- **Scheduling:** Belirli zamanlarda otomatik olarak çalışacak görevler tanımlanabilir.
- **Task State Takibi:** Bir işin bekliyor, çalışıyor veya tamamlandı gibi durumları izlenebilir.

Bu özellikler, Celery’yi basit bir queue yapısından ayırarak tam bir arka plan iş yönetim sistemi haline getirir.

## Redis ile İlişkisi

Celery genellikle Redis ile birlikte kullanılır. Ancak Redis ve Celery aynı şey değildir.

- Redis: veri saklayan ve mesaj kuyruğu olarak kullanılabilen bir sistemdir
- Celery: bu kuyruğu kullanarak işleri yöneten ve çalıştıran sistemdir

Redis, Celery için sadece bir taşıyıcı (broker) görevi görür.

## Redis ile Farkı

Redis ile de bir queue ve worker sistemi kurulabilir. Bu yaklaşımda:

- işler manuel olarak kuyruğa yazılır
- worker mantığı elle yazılır
- hata yönetimi, retry, concurrency gibi özellikler uygulama geliştirici tarafından implement edilir

Bu yöntem düşük seviyeli (low-level) bir yaklaşımdır ve esneklik sağlar. Ancak bakım maliyeti yüksektir ve hataya açıktır.

Celery ise bu altyapıyı hazır olarak sunar. Yüksek seviyeli (high-level) bir abstraction sağlar. Geliştirici sadece yapılacak işi tanımlar, geri kalan süreç Celery tarafından yönetilir.

## Neden Celery Kullanılır

Celery kullanımı şu durumlarda anlamlı hale gelir:

- uzun süren işlemlerin ana uygulamadan ayrılması gerektiğinde
- aynı anda birden fazla işin paralel çalıştırılması gerektiğinde
- hata yönetimi ve retry mekanizmasının güvenilir olması gerektiğinde
- sistemin ölçeklenebilir olması istendiğinde

Celery, uygulama performansını artırmak için değil, işlerin doğru yerde ve doğru şekilde çalıştırılmasını sağlamak için kullanılır.


