from __future__ import absolute_import, unicode_literals

# from celery.decorators import task
from celery import shared_task
from celery.utils.log import get_task_logger

from .email import send_review_email

logger = get_task_logger(__name__)

@shared_task()
def send_review_email_task(name, email, review):
    logger.info('Sent review mail')
    print('r3')
    return send_review_email(name, email, review)

# @periodic_task(
#     run_every=(crontab(minute='*/15')),
#     name="task_save_latest_flickr_image",
#     ignore_result=True
# )
@shared_task
def periodic_mail(name=None, email=None, review='sample message'):
    if name == None or email == None:
        print('process aborted')
        return
    return send_review_email(name, email, review)
