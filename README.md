# DRF Project

REST API проект на **Django + Django REST Framework**.
Реализует базовую структуру backend-приложения с поддержкой CRUD-операций, аутентификации и масштабируемой архитектуры.

---

## 🛠 Стек

- Python 3.13+
- Django
- Django REST Framework
- PostgreSQL
- Pytest
- Docker (опционально)

---

## 🖥️ Локальный запуск проекта (Linux / macOS)

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/takinashida/DRF.git
cd DRF
```

---

### 2️⃣ Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Настройка `.env`

```bash
cp .env_example .env
```


---

### 5️⃣ Запуск проекта через Docker

```bash
docker compose up -d --build
```

Если всё ок — API доступно, миграции можно прогнать внутри контейнера:

```bash
docker compose exec django-backend python manage.py migrate
```
---

Проект будет доступен по адресу:
`http://127.0.0.1:8000/`

Так же сейчас проект доступен в публичном доступе по адресу `http://158.160.215.114/`

---

## 🌍 Запуск проекта на удалённом сервере (Production)

### 1️⃣ Подготовка сервера (Ubuntu 20.04 / 22.04)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git docker.io docker-compose-plugin
```

Добавляем себя в docker-группу:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

### 2️⃣ Клонирование проекта на сервер

```bash
git clone https://github.com/takinashida/DRF.git
cd DRF
```

---

### 3️⃣ Настройка `.env` для production

```bash
cp .env_example .env
nano .env
```

Важно для сервера:

- `DEBUG=False`
    
- нормальный `SECRET_KEY`
    
- отдельные данные БД
    
- `ALLOWED_HOSTS=your_domain_or_ip`
    

---

### 4️⃣ Запуск контейнеров

```bash
docker compose up -d --build
```

После запуска:

```bash
docker compose ps
```

Если всё `Up` — значит сервер запущен

---

### 5️⃣ Миграции и сборка статики

```bash
docker compose exec django-backend python manage.py migrate
docker compose exec django-backend python manage.py collectstatic --noinput
```

---

## 🔄 CI/CD (GitHub Actions)

### Цель:

- при `push` → проверить код и задеплоить на сервер
    

---

### 1️⃣ Secrets в GitHub

В репозитории → **Settings → Secrets → Actions**:

- `SSH_HOST`
    
- `SSH_USER`
    
- `SSH_KEY`
    


---

## 📡 Документация

Базовый URL автогенерируемой API-документации:

```
/materials/api/schema/swagger/
```

---

## 🧪 Тесты

Запуск тестов:

```bash
python /manage.py test
```

---

## 📁 Структура проекта

```
DRF/
├── config/        # Основные настройки Django
├── users/         # Пользователи и аутентификация
├── materials/     # Основная бизнес-логика / API
├── manage.py
└── requirements.txt
```


