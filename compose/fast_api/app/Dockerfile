FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./compose/fast_api/app/start_app.sh /start_app.sh
RUN chmod +x /start_app.sh

COPY .. /app
