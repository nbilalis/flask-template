#!/bin/sh

rm -rf .venv/

python3 -m venv .venv
. .venv/bin/activate

python3 -m pip install --upgrade pip
pip install -r ./requirements.txt
