#!/bin/bash
cd $2
python -m venv .venv
source .venv/bin/activate
pip install $1
