FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./compose/fast_api/worker/start_worker.sh /start_worker.sh
RUN chmod +x /start_worker.sh

COPY . /app
