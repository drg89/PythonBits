@echo off
cd pkg
pip install matplotlib-3.1.1.tar.gz
pip install numpy-1.16.4.zip
pip install qrcode-6.1.tar.gz
cd bin
idle -r "app.py"