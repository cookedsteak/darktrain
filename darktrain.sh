#!/usr/bin/env bash

JPG_FOLDER=${1%*/}
XML_FOLDER=${2%*/}
DES_FOLDER=$JPG_FOLDER"_after"

python3 archive.py -j "$JPG_FOLDER" -x "$XML_FOLDER" -d "$DES_FOLDER"
python3 cleaner.py -j "$DES_FOLDER/JPEGImages" -x "$DES_FOLDER/Annotations"
python3 classify.py -x "$DES_FOLDER/Annotations" -d "$DES_FOLDER"
python3 prepare.py -d "$DES_FOLDER"