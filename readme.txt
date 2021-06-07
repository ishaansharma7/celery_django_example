username:admin
pass:admin1234

enter your email and pass in settings file

1)install redis
2)python3 manage.py runserver
3)celery -A proj worker -l info
4)celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler