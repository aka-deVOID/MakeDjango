@echo on
set arg1=%1
set arg2=%2
cd arg2
python -m venv .venv
source .venv/bin/activate
pip install arg1
