import short_url as shorter
from .models import Url
import os 

def get_absolute_short_path(short_url):
    if os.environ.get("SERVER_PORT"):
        new_short_url = "{}:{}/{}".format(
            os.environ.get("HOST"), os.environ.get("SERVER_PORT"), short_url
        )
    else:
        new_short_url = "{}/{}".format(os.environ.get("HOST"), short_url)

    return new_short_url

def get_clean_short_url(short_url):
    short_url = short_url.split("/")
    short_url = short_url[-1]

    if short_url == "":
        short_url = shorter.encode_url(len(Url.objects.all()))

    return short_url