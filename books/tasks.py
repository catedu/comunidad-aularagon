from celery import shared_task


@shared_task
def who_am_i():
    print("Eres Jesús")