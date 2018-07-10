# Data analysis

## How to use?
* Fork/Clone
* Create and activate a virtual environment - Python-3.6
* Install dependencies - pip install -r requirements
* create a db and change DATABASES settings in settings.py accordingly
* Make migrations - python manage.py makemigrations
* Build the database - python manage.py migrate
* Create a superuser - python manage.py createsuperuser
* Load data to backend db - use import in localhost:admin and upload csv file
* python manage.py createcachetable - #for caching
* Run the development server - python manage.py runserver

#####Home View
* distribution of number of males and females
* number of people in each relationship status. 

<img src="/docs/home.png"/>

#####Home View - without cache
<img src="/docs/sc.png"/>

#####Home from cache
<img src="/docs/home_cache.png"/>

#####Data View
data with filter : sex, race, and relationship

<img src="/docs/data.png"/>



