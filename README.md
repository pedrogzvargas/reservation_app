reservation_app
=======================

**reservation_appt** Es un proyecto hecho en Python y FastApi


Meta
----

Author:
    Pedro Jesús González Vargas

Componentes del proyecto
----

### 1. Python
### 2. RabbitMQ
### 3. PostgreSQL


Uso con docker y docker compose
-----

Para construir el proyecto con  ``docker-compose`` debemos poner los valore correspondiente en ``.env``

    POSTGRES_DB=<value>
    POSTGRES_USER=<value>
    POSTGRES_PASSWORD=<value>
    POSTGRES_DATA=<value>
    DATABASE_URL=<value>
    RABBITMQ_ERLANG_COOKIE=<value>
    RABBITMQ_DEFAULT_USER=<value>
    RABBITMQ_DEFAULT_PASS=<value>
    RABBITMQ_DEFAULT_VHOST=<value>
    RABBITMQ_DIR=<value>
    RABBITMQ_URL=<value>
    RABBITMQ_EXCHANGE_NAME=<value>
    RABBITMQ_EXCHANGE_TYPE=<value>
    RABBITMQ_QUEUE_NAME=<value>
    RABBITMQ_LISTENING_QUEUE_NAME=<value>
    RABBITMQ_ROUTING_KEY=<value>

Existe un archivo de ejemplo en el repositorio y podemos usar el siguiente comando:
    
    $ cp local.env .env

Para construir y levantar los contenedores usamos los comandos:

    $ docker-compose build --no-cache

    $ docker-compose up

Los puertos de docker en local son los siguientes
    
    App -> 8000
    
    Postgres -> 5434

    RabbitMQ -> 15672, 5672


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

Corremos el proyecto con el siguiente comando, ya debemos tenes Postgres y RabbitMQ corriendo:

    $  uvicorn app.main_app:app --reload


En el repositorio ya existe un archivo con 7000 usuarios en el folder ``csv``, pero de igual manera podemos crear un listado de usuarios con un script Python:

    $ python python modules/shared/infraestructure/passenger_data_generator.py


Podemos cargar los usuarios a la base de datos con el siguiente comando, este usa el archivo creado previamente en el folder ``csv``

    $ python modules/shared/infraestructure/load_passenger_data_to_db.py