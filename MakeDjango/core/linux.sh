#!/bin/bash
cd $1
python -m venv .venv
source .venv/bin/activate
shift
pip install "$@"
pip install --upgrade pip
