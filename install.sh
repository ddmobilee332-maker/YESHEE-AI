#!/bin/bash
clear
echo -e "\033[1;31mกำลังจัดเตรียมสภาพแวดล้อมสคริปต์ดั้งเดิม..."
sleep 1
mkdir -p data utils signer
touch data/devices.txt data/models.txt data/proxy.txt
pip install -r requirements.txt
clear
python main.py
