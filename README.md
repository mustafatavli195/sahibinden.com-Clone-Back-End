[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Türkçe](https://img.shields.io/badge/lang-Türkçe-red.svg)](README.tr.md)

# 📌 Sahibinden.com Clone - Back-End

This project is a **backend API** developed using **Django REST Framework (DRF)**. It provides RESTful services that allow users to perform specific operations.

---

## 🚀 Setup and Run  

Follow the steps below to run the project on your local machine.

### 1️⃣ **Clone the Project**  
First, clone the project from GitHub:  
```sh
git clone https://github.com/USER_NAME/REPO_NAME.git
cd sahibinden.com-Clone-Back-End
```

### 2️⃣ **Create and Activate a Virtual Environment (venv)**  
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

### 3️⃣ **Install Required Dependencies**  
```sh
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**  
Create the `.env` file used in the project and fill in the necessary information:  
```sh
cp .env.example .env
```
Edit the content of the `.env` file according to your needs.

### 5️⃣ **Apply Database Migrations**  
```sh
python manage.py migrate
```

### 6️⃣ **Run the Server**  
```sh
python manage.py runserver
```
If the server runs successfully, you can access the API at the following address:  
👉 **http://127.0.0.1:8000/**

---

## 🛠 Technologies Used  
- Django  
- Django REST Framework (DRF)  
- Python  
- SQLite/PostgreSQL (Database)

---

## 📌 Project Description  
This project was developed to create a simple **backend API version** of the Sahibinden.com website, primarily for **practical learning and skill improvement**.

### 📢 Features:  
- Users can **register, log in, and authenticate using JWT**.  
- Users can **add, delete, and update car and real estate ads**.  
- Users can **list ads and view their details**.  
- **JWT token protected and non-protected endpoints** are separated.

---

## 🔑 Authentication and User Operations  
Users log in and are authenticated with **email and password**. A **JWT token** is returned to every user who successfully logs in.

### 📌 User Registration  
**Endpoint:** `POST /api/user/register/`  
```json
{
    "email": "random@hotmail.com",
    "username": "random",
    "password": "123456"
}
```

### 📌 User Login  
**Endpoint:** `POST /api/user/login/`  
```json
{
    "email": "random@hotmail.com",
    "password": "123456"
}
```

> **NOTE:** When making requests to endpoints starting with `api/user/`, the JWT token must be sent in the Headers as **Authorization: Bearer <JWT_TOKEN>**.

---

## 📌 Ad Operations

### 📢 Car Ads

| **Endpoint** | **Method** | **Description** |
|-------------|------------|-----------------|
| `/api/user/car/` | **GET** | Lists the car ads created by the user. |
| `/api/user/car/` | **POST** | Adds a new car ad. |
| `/api/user/car/<int:car_id>/` | **PUT** | Updates the ad with the specified ID. |
| `/api/user/car/<int:car_id>/` | **DELETE** | Deletes the ad with the specified ID. |

**Example POST Request:**  
```json
{
  "title": "Minibus for Sale - Suitable for Student Transport",
  "description": "2018 model, seat layout updated, suitable for student transport..."
}
```

---

Let me know if you need further adjustments!