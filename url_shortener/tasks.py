from django.core.exceptions import ObjectDoesNotExist
from celery import shared_task
from .models import Url 
from django.utils import timezone
from url_shortener_engine.celery import app

@shared_task(name="delete_outdate_url")
def delete_outdate_url():
    try:
        urls = Url.objects.all()
    except ObjectDoesNotExist as e:
        return str(e)

    for url in urls:
        if (url.created_at + timezone.timedelta(days=14)).date() <= timezone.now().date():
            url.delete()

