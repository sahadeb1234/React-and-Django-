# React-and-Django-
Connect React JS Frontend with Django Backend 
# How to run
After cloning the repo, do the following to setup the app
source env/bin/activate
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py runserver
pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.
INSTALLED_APPS = [
    ...
    'rest_framework',
]

 #the django server should now be up and running.
# from the frontend folder, execute those lines:
npm install
npm start
