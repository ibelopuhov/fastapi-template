FROM python:3.9-slim-bullseye

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app /app
COPY ./.env_prod /.env
COPY ./app_config_prod.json /app_config.json

RUN mkdir -p /var/log/app/

WORKDIR /

EXPOSE 5001

CMD ["uvicorn", "app.api.api_app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5001"]