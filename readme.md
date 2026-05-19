# Celery Learning & Real-World Integration

Bu repo Celery öğrenme sürecini temelden başlayarak gerçek dünya backend mimarisine kadar ilerletmek amacıyla oluşturuldu.

Amaç sadece Celery komutlarını öğrenmek değil; asynchronous task mantığını, Redis broker yapısını, worker mimarisini ve production backend sistemlerinde Celery’nin nasıl kullanıldığını anlamaktı.

Repo üç ana bölümden oluşmaktadır.

---

# Repository Structure

```text
Celery/
│
├── 1-celery-fundamentals
├── 2-celery-basic-project
└── 3-celery-fastapi
```

---

# 1 - Celery Fundamentals

Bu bölüm Celery’nin temel çalışma mantığını öğrenmek için oluşturuldu.

İçerikte:

- Celery nedir?
- Background task mantığı
- Synchronous vs Asynchronous farkı
- Redis broker sistemi
- Queue mantığı
- Worker yapısı
- Task lifecycle
- Producer / Consumer modeli
- delay() mantığı

gibi temel konular çalışıldı.

Bu aşamada amaç production proje geliştirmek değil, Celery mimarisini anlamaktı.

---

# 2 - Celery Basic Project

Bu bölüm Celery’nin gerçek çalışma mantığını görmek için hazırlanmış mini pratik projesidir.

Amaç:

- uzun süren işlemleri ana uygulamadan ayırmak
- task queue mantığını görmek
- worker process yapısını anlamak
- retry / concurrency / timeout gibi Celery mekanizmalarını test etmekti

Bu projede:

- app.py üzerinden task üretildi
- Redis queue olarak kullanıldı
- Celery worker queue dinledi
- Task’lar background olarak çalıştırıldı
- Result backend üzerinden state takibi yapıldı

Pratik edilen başlıca özellikler:

- Task Queue
- Worker Process
- Retry
- Error Handling
- Concurrency
- Timeout
- Task State Tracking

Bu bölüm doğrudan production API entegrasyonu yerine Celery’nin hazır sunduğu mekanizmaları anlamaya odaklandı.

---

# 3 - Celery + FastAPI + Kubernetes

Bu bölümde Celery gerçek bir backend mimarisi içine entegre edildi.

Daha önce geliştirilmiş olan:

- FastAPI
- PostgreSQL
- Docker
- Kubernetes
- Redis

altyapısı üzerine Celery eklendi.

Başlangıçta sistem synchronous çalışıyordu.

Kullanıcı oluşturulduğunda activity log kayıtları doğrudan request sırasında PostgreSQL’e yazılıyordu.

Bu yaklaşım production ortamlarında:

- request süresini uzatır
- thread bloklanmasına neden olur
- performans düşürür

Bu nedenle activity log sistemi asynchronous mimariye geçirildi.

---

# Kurulan Architecture

```text
FastAPI
   ↓
Redis Broker / Queue
   ↓
Celery Worker
   ↓
PostgreSQL
```

Akış şu şekilde ilerlemektedir:

1. API request gelir
2. Kullanıcı oluşturulur
3. FastAPI doğrudan DB işlemi yapmak yerine task üretir
4. Redis task queue görevi görür
5. Celery worker queue’dan task’i alır
6. Activity log PostgreSQL’e background olarak yazılır

Bu sayede API request’i log insert işlemini beklemez.

---

# Kubernetes Tarafı

Bu projede Celery worker Kubernetes üzerinde ayrı deployment olarak çalıştırıldı.

Kurulan yapılar:

- FastAPI Deployment
- Celery Worker Deployment
- Redis Deployment
- PostgreSQL StatefulSet
- Kubernetes Services
- Rolling Update
- Health Checks
- Resource Limits

Bu yapı sayesinde gerçek backend orchestration mantığı pratik edildi.

---



# Kullanılan Teknolojiler

- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- Celery
- Docker
- Kubernetes
- Uvicorn

---

