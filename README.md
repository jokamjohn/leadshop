# Leadshop

[![CircleCI](https://circleci.com/gh/jokamjohn/leadshop/tree/master.svg?style=svg)](https://circleci.com/gh/jokamjohn/leadshop/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/jokamjohn/leadshop/badge.svg?branch=master)](https://coveralls.io/github/jokamjohn/leadshop?branch=master)

Leadshop is an e-commerce application which enables a user sign up a merchant and then 
create a shop.

It also enables one to sign up as a buyer and be able to buy goods from 
the available shops on the platform.

## Installation.
- Clone the repository onto your machine.
- Create a virtual environment for the project
- cd into the leadshop folder and install the project dependencies by running
 ```angular2html
pip install -r requirements.txt
```
- Export the following environment variables with the appropriate values
```angular2html
EMAIL_USER
EMAIL_PASSWORD
EMAIL_PORT
EMAIL_HOST
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
```

- Run the database migration by running 
```angular2html
python manage.py migrate
```

- Run the tests using 
```angular2html
python manage.py test
```

- Start the server by running 
```angular2html
python manage.py runserver
```
