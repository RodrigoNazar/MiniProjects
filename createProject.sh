#!/bin/bash

echo "Creando el proyecto $1 ..."

mkdir $1
cd $1

touch requirements.txt 
echo "# Dependencias del proyecto" >> requirements.txt

virtualenv -p python3 venv
. venv/bin/activate

python_version=(which python)

echo $python_version
