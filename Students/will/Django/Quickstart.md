# Quick Start 
#### windows 10

## Django Install w/in Virtual Environment
#### using Virtualenv not Pipenv
- cd to the folder in which you wish for the Virtual environment to exist
- python -m venv myvenv (myvenv is the name chosen for the environ) 
- Install latest pip with python -m pip install --upgrade pip
- create a file requirements.txt at the smae directory level as the virtual environment and save Django~=2.2.4 in it
- pip install -r requirements.txt 
- deactivate to exit myvenv

## Create Django Project
- cd to the folder where the application will live
- enter virtualenv for the project
- create project: django-admin startproject <project_name> .
- create app w/in project: python manage.py startapp <app-name> .
- add <app-name> to INSTALLED_APPS in project directory

