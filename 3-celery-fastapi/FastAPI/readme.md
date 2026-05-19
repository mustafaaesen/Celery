# FastAPI Sample Project (Dockerized)

Bu proje, FastAPI ile geliştirilen **API-only bir backend uygulamasının** PostgreSQL veritabanı ile entegre edilip **Docker & Docker Compose kullanılarak dockerize edilmiş** hâlini göstermektedir.

Amaç; FastAPI ile yazılan bir backend uygulamasının, gerçek dünyada karşılığı olan bir mimariyle nasıl çalıştırıldığını ve dağıtıma hazır hâle getirildiğini küçük ama kapsayıcı bir örnek üzerinden göstermektir.

---

## Projenin Amacı

Bu sample project ile aşağıdaki kavramların birlikte ve uyumlu şekilde kullanılması hedeflenmiştir:

- API-only backend yaklaşımı
- CRUD işlemleri
- Request / response validation
- HTTP status code ve error handling
- User activity (audit / log) mantığı
- PostgreSQL ile kalıcı veri yönetimi
- Alembic ile veritabanı migration yönetimi
- Docker ve Docker Compose ile container tabanlı çalışma

---

## Genel Mimari

Uygulama Docker Compose ile tanımlanmış iki ana bileşenden oluşur:

- **FastAPI API servisi**
- **PostgreSQL veritabanı**

Bu servisler aynı Docker network üzerinde haberleşir.  
Uygulama yapılandırmaları `.env` dosyası üzerinden yönetilir.

---

## Uygulama Yapısı

Uygulama içerisinde iki temel alan bulunmaktadır:

- **Users**
  - Kullanıcı ekleme
  - Kullanıcı listeleme
  - Kullanıcı silme

- **Activities**
  - Sistem üzerinde gerçekleşen önemli aksiyonların
    (kullanıcı oluşturma, silme vb.)
    activity log olarak kayıt altına alınması

Tüm işlemler FastAPI endpoint’leri üzerinden gerçekleştirilir ve Swagger UI ile test edilebilir.

---

## Veritabanı ve Migration Yönetimi

- Veritabanı olarak **PostgreSQL** kullanılmaktadır
- ORM katmanı **SQLAlchemy** ile oluşturulmuştur
- Veritabanı şeması **Alembic** ile versionlanmaktadır
- Migration işlemleri Docker container içinden yönetilmektedir

Oluşturulan temel tablolar:

- `users`
- `user_activities`
- `alembic_version`

---

## Docker ve Çalıştırma

Proje Docker ve Docker Compose kullanılarak çalıştırılmaktadır.

Uygulamayı ayağa kaldırmak için:

```bash
docker compose up -d
```

FastAPI servisinin ayağa kalkmasından sonra Swagger UI üzerinden endpoint’ler test edilebilir:

```text
http://localhost:8000/docs
```

---

## Swagger Üzerinden Test

Swagger arayüzü üzerinden:

- Kullanıcı ekleme (POST)
- Kullanıcı listeleme (GET)
- Kullanıcı silme (DELETE)
- Activity kayıtlarını görüntüleme

işlemleri test edilmiştir.

Swagger ekran görüntüsü:  
`screenshots/project1.png`
`screenshots/project2.png`
---

## Kullanıcı ve Activity Akışı

Uygulama üzerinde:

- Kullanıcı oluşturma
- Kullanıcı listeleme
- Kullanıcı silme

işlemleri gerçekleştirilmiş ve bu aksiyonların **activity log** olarak kaydedildiği doğrulanmıştır.

Kullanıcı listesi ve activity kayıtları Swagger üzerinden görüntülenmiştir.

---

## Kazanımlar

Bu proje ile:

- FastAPI ile modüler API geliştirme
- PostgreSQL entegrasyonu
- Alembic ile migration yönetimi
- Docker Compose ile multi-service yapı
- Environment-based configuration kullanımı
- Gerçek dünyada sık kullanılan activity log mantığı

tek bir mini proje içerisinde bir araya getirilmiştir.

Bu çalışma, FastAPI öğrenme sürecinde geliştirilen bir backend uygulamasının **dockerize edilerek gerçek dünyaya yakın bir hâle getirilmesini** amaçlayan tamamlayıcı bir örnektir.
