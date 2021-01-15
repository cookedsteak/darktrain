#!/usr/bin/env bash

FOLDER=${1%*/}
DES_FOLDER=${2%*/}
echo "$FOLDER"
if [ "${DES_FOLDER}" == "" ];then
  DES_FOLDER=$FOLDER"_after"
fi

python3 archive.py -j "$FOLDER" -x "${FOLDER}/xml" -d "$DES_FOLDER"
