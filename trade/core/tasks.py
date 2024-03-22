"""

from celery import shared_task
from django.core.management import call_command

@shared_task
def send_promotional_emails():
    call_command('send_promotional_emails')


"""