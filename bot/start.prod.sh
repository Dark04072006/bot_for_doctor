#! /bin/bash

mkdir -p logs/
mkdir -p locales/

. ../env/env.sh
. ../.prod_bot/bin/activate

export BOT_MODE='production'
pybabel compile -d locales -D bot

exec python app.py
