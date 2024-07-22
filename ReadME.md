# Department Employees Tree Project

## Технические требования

- Python 3.5+
- Django 3+
- PostgreSQL

## Установка

1. Создайте виртуальное окружение и активируйте его:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

3. Создайте файл .env. Настройте базу данных в файле .env:
   ```dotenv
    DEBUG=true
    SECRET_KEY=secret-key
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
   ```

4. Выполните миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

## Генерация тестовых данных

Для генерации используйте скрипт `generate_data.py`:

```bash
python generate_data.py
```

Этот скрипт создаст:
- 25 отделов (5 уровней по 5 отделов на каждом уровне)
- 50 000 сотрудников с реалистичными данными

## Запуск проекта

1. Запустите сервер разработки:
   ```
   python manage.py runserver
   ```

2. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/` для просмотра древовидной структуры отделов.

3. Для доступа к административной панели перейдите по адресу `http://127.0.0.1:8000/admin/` и войдите, используя созданные вами учетные данные суперпользователя.

## Структура проекта

```
department-project/
│
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── apps/
│   ├── __init__.py
│   ├── urls.py
│   ├─employees/
│     ├── migrations/
│     ├── __init__.py
│     ├── admin.py
│     ├── apps.py
│     ├── models.py
│     ├── tests.py
│     ├── urls.py
│     └── views.py
│   
├── templates/
│   └── employees/
│       └── tree.html
│
├── manage.py
├── .gitignore.py
├── generate_data.py
├── requirements.txt
└── README.md
```
