from celery import shared_task
from celery.utils.log import get_task_logger
from .emails import send_email
logger = get_task_logger(__name__)


@shared_task(name='send_review_task')
def send_review_task(subject, email, review):
    logger.info("Email Sent. ")
    return send_email(subject, email, review)


