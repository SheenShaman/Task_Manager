# Проект Task Manager

Task Manager - серверное приложение для работы с базой данных.

## Технологии:

* python 3.11
* fastapi 0.108.0
* pydantic 2.5.3
* alembic 1.13.1
* psycopg2 2.9.9
* SQLAlchemy 2.0.24

## Установка:

Для установки и запуска проекта выполните следующие шаги:

1. Склонируйте репозиторий проекта на свой локальный компьютер git clone _https://github.com/SheenShaman/Task_Manager_
2. Создайте виртуальное окружение **python3 -m venv venv**
3. Активируйте виртуальное окружение **venv\Scripts\activate**
4. Установите зависимости **pip install -r requirements.txt**
5. Создайте Базу данных (в данной работе используется PostgreSQL)
6. перейдите в **.env.sample** и пропишите переменные окружения
7. После создания пропишите команду для применения миграций **alembic upgrade head**
8. Для запуска сервера пропишите в терминале **uvicorn src.main:app --reload**

##### В проекте используется Docker Compose

Для запуска приложения необходимо выполнить следующие команды:

* **docker-compose build** - сборка образа
* **docker-compose up** - запуск контейнера

###### Автор проекта:

https://github.com/SheenShaman