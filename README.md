reservation_app
=======================

**reservation_appt** Es un proyecto hecho en Python y FastApi


Meta
----

Author:
    Pedro Jesús González Vargas


Elementos
----

Author:
    Pedro Jesús González Vargas

Uso con docker y docker compose
-----

Para construir el proyecto con  ``docker-compose`` debemos poner los valore correspondiente en ``.env``

    POSTGRES_USER=<value>
    POSTGRES_PASSWORD=<value>
    POSTGRES_DATA=<value>
    DATABASE_URL=<value>
    RABBITMQ_DIR=<value>
    RABBITMQ_URL=<value>
    RABBITMQ_EXCHANGE_NAME=<value>
    RABBITMQ_EXCHANGE_TYPE=<value>
    RABBITMQ_QUEUE_NAME=<value>
    RABBITMQ_ROUTING_KEY=<value>

Para construir y levantar los contenedores usamos los comandos:

    $ docker-compose build --no-cache

    $ docker-compose up

Uso con entorno virtual local
-----

Debemos tener una instalación de Postgres y RabbitMQ

Debemos poner los valores correspondiente en nuestro archivo ``.env``

Existe un archivo de ejemplo en el repositorio y podemos usar el siguiente comando:
    
    $ cp local.env .env
    
Creamos un entorno virtual, en caso de usar pyenv el comando es el siguiente:

    $ pyenv virtualenv 3.9.0 reservation_app

Debemos de agregar la configuracion en nuestro IDE, o en su defecto activar nuestro entorno virtual.

Instalamos los requerimientos:

    $ pip install -r requirements.txt

Corremos el proyecto con el siguiente comando:

    $  uvicorn app.main_app:app --reload
