# Базовый шаблон приложения FastAPI

Шаблон для создания приложения с использованием фреймворка [FastAPI](https://fastapi.tiangolo.com/)

## Разработка приложения

* создать вртуальную среду python 3.8+ и набор требуемых для текущей разработки библиотек

```shell
python3 -m venv api-venv
source api-venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install --upgrade setuptools wheel
pip3 install -r requirements.txt
```

## Тестирование приложения

Для запуска тестов используется pytest. Тесты находятся в папке tests. Запускаются тесты следующим образом из корневой папки проекта:

как пользоваться [Pytest](https://docs.pytest.org/en/latest/how-to/usage.html)

* все тесты из папки:

```shell
python3 -m pytest tests
```

* только выбранные тесты

```shell
python3 -m pytest tests/test_func.py
```

## Запуск приложения

* Запуск программы prod:  
`uvicorn app.api.api_app:app --host 0.0.0.0 --port 5001`

* Запуск программы dev (with automatic reloads on code changes):  
`uvicorn app.api.api_app:app --host 0.0.0.0 --port 5001 --reload`

* Страница openapi приложения: [http://localhost:5001/docs](http://localhost:5001/docs)

## Билдование образов docker

* Билдование основного образа:  
`docker build --rm=true -t my-service:latest .`

* Билдование образа на основе ubuntu:latest (больше по размеру)  
`docker build -f Dockerfile_ubuntu --rm=true -t my-service:latest-ubuntu .`

## Работа с образами докера

### Загрузка и сохранение

* сохранение образа для экспорта  
`docker save my-service:latest | gzip > my-service-latest.img.gz`

* загрузка образа на целевой машине  
`cat my-service-latest.img.gz | docker load`

### Запуск приложения с использованием утилиты `docker-compose`

* production:  
start: `docker-compose up -d`  
stop: `docker-compose down`  
log: `docker-compose down logs -f`

* development  
start: `docker-compose -f docker-compose-dev.yml up -d`  
stop: `docker-compose -f docker-compose-dev.yml down`  
log: `docker-compose -f docker-compose-dev.yml logs -f`
