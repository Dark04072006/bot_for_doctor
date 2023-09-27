#! /bin/bash

mkdir -p logs/
mkdir -p locales/

. ../env/env.sh
. ../.dev_bot/bin/activate

export BOT_MODE='development'

exec watchmedo auto-restart -R -p '*.py' -- python app.py
