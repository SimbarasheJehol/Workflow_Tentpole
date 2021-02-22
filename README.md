# Workflow_Tentpole
This application is a django application that takes in customer information(Name ,surname ,date of birth and an excel file) and renders a graph showing customer expinditure per month.

# Usage
1.Make sure to install python 3+ first in your system.

2.Excute the following commands in the terminal.
    
    pip install django
    pip install django-crispy-forms

3.Then make sure in the terminal you change directory into tentpoleworkflow such that you can see manage.py file and then excute the following:
    
    python manage.py migrate
    python manage.py runserver
    
4.Then go to the browser and open local address

    http://127.0.0.1:8000/
    
# Assumptions 
1. The excel Sheet to hold customer expinditure is named Sheet1
2. Assuming the user will upload an excel file when choosing a file to upload 
