# PDF To Text Converter

## Approach

I had to create a PDF to text converter where user can save his pdf and convert it to text.

So i started with creating user login and resgistration API's

After that I created API's to upload and save PDF's

Then I added logic to Convert pdf to text and save it using serializers

After that i created Api to Retrive the pdf and texts uploaded by logged in user

##  Challenges 


### Setting Foreign Keys

I was facing issue retriving the PK's i resolved it using filter 

### Getting Url to pdf

I was able to get latest pdf uploaded by logged in authenticated user but i wasnt able to get url from that
Actually i was getting a queryset so i got particuler object by adding filter(user=request.user).latest('id')
Then i got the url by obj.url and i was good to go

### Authenitcation 

I was facing issues here so i used knox for authentication

## Installation

First Clone the repo and go to the directory
Then create a virtual environment
```bash
  python -m venv env
```
Acticate the virtual environment 
```bash
  env/scripts/activate
```
Install dependancies
```bash
  pip install -r requirements.txt
```
Add your postgres credentials in the settings.py
Then run migrations
```bash
 python manage.py migrate
```
Create a superuser
```bash
  django-admin createsuperuser
```
Start the devlopment server
```bash
  python manage.py runserver
```
Go to localhost:8000/login
And you are good to go
