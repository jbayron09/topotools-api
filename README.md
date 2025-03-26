#Premium api

## Initial setup
1. Be sure of your virtual environment is activated
2. Run `pip install -r requirements.txt`
3. Run `python manage.py migrate`
4. Run `python manage.py createsuperuser`

## Load categories
To populate database with Categories, run `python manage.py loaddata fixtures/categories.json`

## Load cities
To populate database with cities, run `python manage.py cities_light`