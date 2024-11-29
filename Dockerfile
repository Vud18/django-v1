# Используем базовый образ с Python
FROM python:3.11
# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libmariadb-dev gcc && \
    apt-get clean
# Устанавливаем рабочую директорию
WORKDIR /app/django_project

COPY requirements.txt .
# Копируем файлы проекта
# Устанавливаем зависимости Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application", "python manage.py migrate"]

