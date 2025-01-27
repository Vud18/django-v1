# Проект по созданию веб-страницы с Bootstrap 5 и Django
![Демонстрация слайдера](https://i.ibb.co/5KnXL7v/image.png)
Данный проект реализует веб-страницу на основе предоставленного макета из Figma, используя Django, MySQL и Bootstrap 5. 

Слайдер на странице реализован с использованием библиотеки [Slick Slider](http://kenwheeler.github.io/slick/) (Slider Syncing), а его данные настраиваются через админку Django.

## Функциональные требования

- **Фронтенд**:
  - Используется Bootstrap 5 для верстки страницы.
  - Слайдер реализован через Slick Slider и поддерживает:
    - Синхронизацию миниатюр и большого изображения.
    - Открытие большого изображения в полноэкранном режиме и возможность листать фотографии как галерею.

- **Бэкенд**:
  - Управление слайдером осуществляется через Django Admin:
    - Для загрузки изображений используется пакет `django-filer`.
    - Для кадрирования изображений в админке и на клиентской стороне используется пакет `easy-thumbnails`.
    - Элементы слайдера сортируются через drag&drop благодаря `django-admin-sortable2`.
    - В списке элементов слайдера отображаются миниатюра изображения и название.


## Установка

1. Клонируйте репозиторий
```bash
https://github.com/Vud18/django-v1.git
```
2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Запуск через docker
```bash
docker-compose build

docker-compose up
```

4. Что бы добавить картинки на главный экран, нужно создать суперпользователя.
В консоли введите docker exec -it django_app /bin/bash
затем создайте суперпользователя python manage.py createsuperuser
Вход в систему будет доступен по адресу: http://127.0.0.1:8000/admin

Использование: Перейдите по адресу http://127.0.0.1:8000/
