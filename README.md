# currency_converter
## A simple Currency Converter App in Django which allows only logged in user to access the page.

### for this project following installations are required:
- python 3.12.1

### for this project following commands are required:
- pip install django
- pip install django-admin
- pip install django-crispy-forms
- pip install django-messages
- pip install crispy-bootstrap5

### To accessing admin side of the project following steps are required:
- run python manage.py createsuperuser
- Enter your desired username and press enter.
- You will then be prompted for your desired email address
- The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first
- go to http://127.0.0.1:8000/admin/
- login with same username and password
- go to users and it is showing all the registered users

### To run project:
- python manage.py migrate
- py manage.py runserver
- for registration go to http://127.0.0.1:8000/register
- for login go to http://127.0.0.1:8000/login
- go to http://127.0.0.1:8000/ (It will not allow if user is not logged in or registered).


### Login Page:
![Screenshot (5)](https://github.com/deepsanghani/currency_converter/assets/59606437/d64e989e-08e0-4796-8695-fe0ba52791dd)

### Register Page:
![Screenshot (6)](https://github.com/deepsanghani/currency_converter/assets/59606437/7a0314cd-7749-4642-950e-afec7d678b09)

![Screenshot (7)](https://github.com/deepsanghani/currency_converter/assets/59606437/264d100f-f1e7-460e-8df6-3cea4e04c08e)

### Home Page:
![Screenshot (8)](https://github.com/deepsanghani/currency_converter/assets/59606437/aa009e71-4510-4718-81f0-f93820882c4f)

