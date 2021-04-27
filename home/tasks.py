from celery import shared_task


@shared_task
def count_hompage():
    return "ouuuu mama"