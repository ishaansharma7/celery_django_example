# Celery_Django_Example

This project was created using python 3.8.5

## Requirements
Create virtual environment.\
Install requirements.txt file present in root directory.\
Then install redis server.\
Do appropriate changes in settings.py file

## Run Project

Using the below command run developent server.

#### `python manage.py runserver`

Run celery worker in new terminal.

#### `celery -A Wealthifyme_API worker -l info`

Then run celery beat database scheduler in new terminal.

##### `celery -A Wealthifyme_API beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
