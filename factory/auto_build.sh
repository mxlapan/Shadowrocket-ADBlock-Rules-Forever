#!/bin/bash
set -e

cd ./factory

python3 ad.py
python3 gfwlist.py
python3 build_confs.py
python3 gen_qrcode.py
