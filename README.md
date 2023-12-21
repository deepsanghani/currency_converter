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
- pip install mysqlclient

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
![Screenshot (5)](https://github.com/deepsanghani/currency_converter/assets/59606437/eddfb878-4f48-4495-b7d6-770c21ed8041)


### Register Page:
![Screenshot (6)](https://github.com/deepsanghani/currency_converter/assets/59606437/f67ca2af-9069-4ab9-a19a-0e5304a39563)

![Screenshot (7)](https://github.com/deepsanghani/currency_converter/assets/59606437/70afd45e-856c-4c2d-85f3-c4b897ac2442)


### Home Page:
![Screenshot (10)](https://github.com/deepsanghani/currency_converter/assets/59606437/be8a8557-af26-466d-8291-c9a6211b4e39)


- Whenever user clicks on submit button data gets added to mysql database - Table name - events with timestamp
  ![Screenshot (9)](https://github.com/deepsanghani/currency_converter/assets/59606437/931703f0-fc49-41d3-a18d-8a3b085ae36c)

  ![Screenshot (11)](https://github.com/deepsanghani/currency_converter/assets/59606437/e53967d0-5268-436a-a1d8-276bd60743aa)



