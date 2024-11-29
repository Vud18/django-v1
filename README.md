
## Установка
### 1. Клонируйте репозиторий
https://github.com/Vud18/django-v1.git
### 2. Запуск через docker

Команда 1: docker-compose build

Команда 2: docker-compose up

### 3. Что бы добавить картинки на главный экран, нужно создать суперпользователя.
В консоли введите docker exec -it django_app /bin/bash
затем создайте суперпользователя python manage.py createsuperuser
Вход в систему будет доступен по адресу: http://127.0.0.1:8000/admin

Использование: Перейдите по адресу http://127.0.0.1:8000/
