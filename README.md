docker exec -it django_app /bin/bash миграции
python manage.py migrate миграции

Создание супер пользователя:
docker exec -it django_app /bin/bash
python manage.py createsuperuser
