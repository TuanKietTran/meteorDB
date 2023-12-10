#!/bin/bash

set -euf

airflow db migrate
airflow connections import init/dev_connections.yaml

airflow users create \
        --username admin \
        --password admin \
        --firstname Admin \
        --lastname admin \
        --role Admin \
        --email admin@example.org