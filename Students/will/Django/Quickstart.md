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

## Set up static files, base HTML, and JS and CSS files
### Template HTML
- create templates directory at the project level
- inside templates create pages directory
- inside pages directory create home.html and about.html
- in each file extend base.html {% %}
- lastly in the project's settings.py ammend TEMPLATES DIR with os.path.join(BASE_DIR, 'templates')
### Static files
- at project level create static directory
- w/in static directory create a JS directory and a CSS directory
- w/in js dir create file main.js and css dir create file site.css
- w/in file site.css code h1{color:firebrick;} 
- w/in file main.js code console.log("hello from main.js");
- lastly in the project's settings.py, below STATIC_URL add the line STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
 




