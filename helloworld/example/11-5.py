@celery.task()
def add_together(a, b):
    return a + b