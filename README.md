<h1 align="center">
  <br>
  <a href="https://github.com/luisfelipe7/Learning-Python3.git"><img src="https://rawgit.com/luisfelipe7/Learning-Django/master/django.png" alt="Markdownify" width="200"></a>
  <br>
  Learning Django
  <br>
</h1>
<h4 align="center">Creating a Django project with the tutorial given on the official website of <a href="https://www.djangoproject.com/" target="_blank">Django</a>.</h4>

<p align="center">
  •<a href="#key-features">&nbsp; Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#run-it">Run it</a> •
  <a href="#how-to-use-it">How to use it</a> •
  <a href="#credits">Credits</a>
</p>

## Key Features

* A public site that lets people view polls and vote in them.
* An admin site that lets you add, change, and delete polls.

## Installation

1. Donwload Python 3 from https://www.python.org/downloads/.
2. Install Pip with this link: https://pip.pypa.io/en/stable/installing/ , if you
   don't know if you have pip, type this command
```bash
# Verify pip
$ pip -V
```
   Once you have pip installed, update pip with this command
```bash
# Update pip
$ pip install -U pip
```    
3.  Download or clone this repository in your folder
```bash
# Clone this repository
$ git clone https://github.com/luisfelipe7/Learning-Django
```
3. Go into the repository
```bash
# Go into the repository
$ cd Learning-Django
```

4. Create a virtual environment
```bash
# Install virtualenv 
$ sudo pip install virtualenv 
```
```bash
# Create a virtual environment with Python3, env is the name of the environment
$ virtualenv env --python=python3 
```
```bash
# Activate your environment
$ cd env
$ source bin/activate 
```
 5. With the activated environment, install the requirements:
 ```bash
# Install requirements
$ pip install -r requirements.txt
```
  6. Run it.

## Run it
1. Configure your database and sync your models
```bash
# Apply Migrations
$ python manage.py migrate
```
2. Create a superuser for admin views
```bash
# Create a superuser
$ python manage.py createsuperuser
```
3. Run your development server
```bash
# Run a development server
$ python manage.py runserver
```

## How to use it

Enter to this URL's:
* http://127.0.0.1:8000/polls/
* http://127.0.0.1:8000/polls/idOfTheQuestion

## Credits

Thanks to Django for the tutorial given on the official website.

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

---

> GitHub [@luisfelipe7](https://github.com/luisfelipe7) &nbsp;&middot;&nbsp;
