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

## 🚀 Запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/takinashida/DRF.git
cd DRF
````

### 2. Виртуальное окружение и зависимости

```bash
python -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Переменные окружения

Создай файл `.env` на основе `.env_example` и укажи необходимые значения.

### 4. Запуск

```bash
docker compose up -d --build
```

Проект будет доступен по адресу:
`http://127.0.0.1:8000/`

Так же сейчас проект доступен в публичном доступе по адресу `http://158.160.215.114/`

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


