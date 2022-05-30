#! /bin/bash
git clone https://github.com/Kesha123/automation.git
cd automation
touch config.env
echo -e '[DOWNLOAD]\nDOWNLOAD_DIR="Downloads"' > config.env
python3 -m venv .
case "$OSTYPE" in
    linux*)   source bin/activate;;
    msys*)    \Scripts\activate.bat ;;
    cygwin*)  echo "ALSO WINDOWS" ;;
    darwin*)  source bin/activate ;; 
esac
pip install -r requirements.txt
python3 LeApp.py -h