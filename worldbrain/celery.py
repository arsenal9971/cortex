from celery import Celery

from django.conf import settings

app = Celery('worldbrain')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def hello_world_task(self):
    print('Request: {0!r}'.format(self.request))
