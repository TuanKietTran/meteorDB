# First time setup

What to do to setup this repo for the first time:

## Step 1: Clone the repo

Using the terminal, clone the repo at a directory

```shell
$ git clone https://github.com/TuanKietTran/meteorDB.git
$ cd meteorDB
```

## Step 2: Start Docker infrastructures

Airflow needs a database for storing its data. For local dev, we will spawn up a PostgreSQL instance using Docker. This assumes that you have already installed and have basic knowledge of Docker.

```shell
$ docker compose -f ./docker-compose.yaml up -d
```

## Step 3: Clone `.env` from `.env.dev.example`

```shell
$ cp .env.dev.example .env
```

## Step 4: Source `.env`

To config Airflow, we will use environment variable. One way to do this is to run:

```shell
# For Bash shell
$ echo '[[ -f .env ]] && source .env' >> ~/.bashrc

# For Zsh shell
$ echo '[[ -f .env ]] && source .env' >> ~/.zshrc
```

If using Oh My Zsh, you can use the [`dotenv` plugin](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dotenv)

## Step 5: Install Python libraries

```shell
$ pip install -r requirements.txt -r requirements.dev.txt
```

## Step 6: Initialize local Airflow

In the terminal, run:

```shell
$ ./bin/init-airflow.
```

Your local development environment should now be ready.
