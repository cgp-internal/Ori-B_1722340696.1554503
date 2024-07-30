#!/bin/bash

# Install Python
python_version="3.9.7"
wget https://www.python.org/ftp/python/$python_version/Python-$python_version.tar.xz
tar -xvf Python-$python_version.tar.xz
cd Python-$python_version
./configure --enable-optimizations
make -j 2
sudo make altinstall

# Install dependencies from requirements.txt
sudo python3.9 -m pip install -r requirements.txt

# Run the Flask server
python3.9 app.py