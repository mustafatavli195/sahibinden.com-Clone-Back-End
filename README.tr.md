[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Türkçe](https://img.shields.io/badge/lang-Türkçe-red.svg)](README.tr.md)

# 📌 Sahibinden.com Clone - Back-End

Bu proje, **Django REST Framework (DRF)** kullanılarak geliştirilmiş bir **backend API**'dir. Kullanıcıların belirli işlemleri yapmasını sağlayan RESTful servisler sunar.

---

## 🚀 Kurulum ve Çalıştırma  

Aşağıdaki adımları takip ederek projeyi kendi bilgisayarınızda çalıştırabilirsiniz.

### 1️⃣ **Projeyi Klonlayın**  
Öncelikle GitHub üzerinden projeyi klonlayın:  
```sh
git clone https://github.com/KULLANICI_ADI/REPO_ADI.git
cd sahibinden.com-Clone-Back-End
```

### 2️⃣ **Sanal Ortamı (venv) Oluşturun ve Aktif Edin**  
- **Windows:**  
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3️⃣ **Gerekli Bağımlılıkları Yükleyin**  
```sh
pip install -r requirements.txt
```

### 4️⃣ **Çevresel Değişkenleri Ayarlayın**  
Projede kullanılan `.env` dosyasını oluşturup gerekli bilgileri girin:  
```sh
cp .env.example .env
```
`.env` dosyasının içeriğini kendinize göre düzenleyin.  

### 5️⃣ **Veritabanı Migrasyonlarını Uygulayın**  
```sh
python manage.py migrate
```

### 6️⃣ **Sunucuyu Çalıştırın**  
```sh
python manage.py runserver
```
Sunucu başarıyla çalıştıysa, API’ye şu adresten erişebilirsiniz:  
👉 **http://127.0.0.1:8000/**

---

## 🛠 Kullanılan Teknolojiler  
- Django  
- Django REST Framework (DRF)  
- Python  
- SQLite/PostgreSQL (Veritabanı)  

---

## 📌 Proje Açıklaması  
Bu proje, **pratik yapmak ve becerileri geliştirmek amacıyla** Sahibinden.com sitesinin basit bir **backend API versiyonunu** oluşturmak için geliştirilmiştir.  

### 📢 Özellikler:  
- Kullanıcı **kayıt olabilir, giriş yapabilir ve JWT ile kimlik doğrulaması yapabilir**.  
- **Araç ve emlak ilanları ekleyebilir, silebilir ve güncelleyebilir**.  
- **İlanları listeleyebilir ve detaylarını görüntüleyebilir**.  
- **JWT token doğrulama gerektiren ve gerektirmeyen endpointler** ayrılmıştır.  

---

## 🔑 Kimlik Doğrulama ve Kullanıcı İşlemleri  
Kullanıcılar **e-posta ve şifre** ile giriş yapıp doğrulanır. Başarıyla giriş yapan her kullanıcıya **JWT token** döner.  

### 📌 Kullanıcı Kayıt Olma  
**Endpoint:** `POST /api/user/register/`  
```json
{
    "email": "random@hotmail.com",
    "username": "random",
    "password": "123456"
}
```

### 📌 Kullanıcı Girişi  
**Endpoint:** `POST /api/user/login/`  
```json
{
    "email": "random@hotmail.com",
    "password": "123456"
}
```

> **NOT:** `api/user/` ile başlayan endpointlere istek atarken JWT token **Authorization: Bearer <JWT_TOKEN>** şeklinde Headers kısmında gönderilmelidir.

---

## 📌 İlan İşlemleri

### 📢 Araç İlanları

| **Endpoint** | **Metod** | **Açıklama** |
|-------------|---------|-------------|
| `/api/user/car/` | **GET** | Kullanıcının oluşturduğu araç ilanlarını listeler. |
| `/api/user/car/` | **POST** | Yeni bir araç ilanı ekler. |
| `/api/user/car/<int:car_id>/` | **PUT** | Belirtilen ID’ye sahip ilanı günceller. |
| `/api/user/car/<int:car_id>/` | **DELETE** | Belirtilen ID’ye sahip ilanı siler. |

**Örnek POST İsteği:**  
```json
{
  "title": "Minibüs Satılık - Öğrenci Taşımaya Uygun",
  "description": "2018 model, koltuk düzeni yenilenmiş, öğrenci taşımacılığı için h...
```

