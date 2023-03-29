#! /usr/bin/bash

url=$1
name=$2 
qr $url > $name'.png'

python3 qr_generator.py $url $name