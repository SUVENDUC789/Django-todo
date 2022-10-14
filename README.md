# Django-todo

(just for practice). You can visit to see my hosted page.

# [Live](https://crud-django-suvenduc.herokuapp.com/ "my heroku-app")

## Deploying Process
## Video Tutorial
[Click here to see the video](https://youtu.be/fH2S5lWNKaM "heroku deployment for django-sqlite3 app")

## Textual
1. At first [create account](https://www.heroku.com "heroku.com") or [login](https://id.heroku.com/login "heroku login") in heroku
1. Download `heroku-cli` from [here](https://cli-assets.heroku.com/heroku-x64.exe "install heroku-cli") or [visit the website](https://devcenter.heroku.com/articles/heroku-cli#download-and-install "click here")

### 3. Create a virtual environment:
```terminal
pip install virtualenv
```
```terminal
virtualenv anyname
```
- After creating virtual environment activate your vitualenv
```terminal
pip install django gunicorn django-heroku
```

`You can install specific version like pip install django==2.2`

- Copy / Transfer your django-project in that virtual environment
- Add your dependencies to requirements.txt by typing in the terminal
```bash
pip freeze > requirements.txt
```

### 4. Setup your django-project before starting `heroku-deployment`
- Don't forget to add this in **settings.py**
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
```
### First, and most importantly, Heroku web applications require a `Procfile`

- _**This file is used to explicitly declare your application’s process types and entry points. It is located in the root of your repository**_

#### Procfile
```
web: gunicorn yourprojectname.wsgi:application --log-file -
```
- Add the following `import` statement to the top of `settings.py`
```python
import django_heroku
```
- Then add the following to the bottom of `settings.py`
```python
# Activate Django-Heroku.
django_heroku.settings(locals())
```
- You can also made these changes in `settings.py`
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*", "localhost"]

# Application definition
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # --> only add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### 5. Final process of `heroku-deployment` for your django-sqlite application
- **Open your terminal / cmd and run the following commands**
```
heroku login
```
- After run `heroku login` your default browser will be open and after logged in heroku you can see:
```
C:\Users\SUPRATIM\Desktop\UselessDjangoApp>heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/e1625921-dddc-400f-adc3-8f570d48ad0c?requestor=SFMyNTY.g2gDbQAAAAw0OS4zNy4zOS4yNTBuBgCYFdJzfgFiAAFRgA.enp9fW26_s1Hzn_VloGHmZpz3hi9QEY07WSUne6sOc4
Logging in... done
Logged in as supratimm531@gmail.com
```
- Now create your `heroku-app` using this command
```
heroku create yourappname
```
- After run this command you can see:
```
C:\Users\SUPRATIM\Desktop\UselessDjangoApp>heroku create yourappname
Creating app... done, yourappname
https://yourappname.herokuapp.com/ | https://git.heroku.com/yourappname.git
```
- **Now follow these steps**
```bash
git status
git init
git remote add heroku https://git.heroku.com/yourappname.git
git remote -v

git status
git add .
git status
git commit -m "initial commit by yourname"
```
- Add `runtime.txt` in the root folder of your project / repository and write the current python version (used for your project) in the file
```
python-3.9.4
```

---
## Caution:
- **If you are using `django==2.2` then change the version of `psycopg2==2.9.x` with `psycopg2==2.8.6` like this**
```bash
pip uninstall psycopg2==2.9.x && pip install psycopg2==2.8.6
```
```bash
pip freeze > requirements.txt
```
- **After this check your `requirements.txt` at-least once**
```
dj-database-url==0.5.0
Django==2.2
django-heroku==0.3.1
gunicorn==20.1.0
psycopg2==2.8.6
pytz==2021.3
sqlparse==0.4.2
whitenoise==5.3.0
```
---

### 6. Your `heroku-app` is now ready to deploy
**Just run this command in your terminal / cmd**
```bash
git push heroku master
```

### 7. Migrate your database-model in your `heroku-app`
**Run these 2 following commands**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

