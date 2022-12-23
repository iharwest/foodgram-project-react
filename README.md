# Foodgram - продуктовый помощник

## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

Описание проекта
----------
«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты, подписываться на публикации других авторов и добавлять рецепты в избранное. Сервис «Список покупок» позволит пользователю создавать список продуктов, 
которые нужно купить для приготовления выбранных блюд.

Системные требования
----------
* Python 3.6+
* Docker
* Works on Linux, Windows, macOS

Запуск проекта в контейнере
----------
Клонируйте репозиторий и перейдите в него в командной строке.
Создайте и активируйте виртуальное окружение:
```
git clone https://github.com/iharwest/foodgram-project-react.git
cd foodgram-project-react
```
Должен быть свободен порт 8000. PostgreSQL поднимается на 5432 порту, он тоже должен быть свободен.
Cоздать и открыть файл .env с переменными окружения:
```
cd infra
touch .env
```
Заполнить ```.env``` файл с переменными окружения по примеру:
```
DB_ENGINE=django.db.backends.postgresql >> .env

DB_NAME=postgres >> .env

POSTGRES_PASSWORD=postgres >> .env

POSTGRES_USER=postgres >> .env

DB_HOST=db >> .env

DB_PORT=5432 >> .env

SECRET_KEY=************ >> .env
```
Установить и запустить приложения в контейнерах:
```
docker-compose up -d
```
Запустить миграции, создать суперюзера, собрать статику и заполнить БД:
```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input 

docker-compose exec backend python manage.py load_data ingredients.csv
```
Документация к проекту
----------
Документация для API после установки доступна по адресу 

```http://127.0.0.1/api/docs/```

Автор: [Николаев Алексей](https://github.com/iharwest)