from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import parse_page
from django.utils import timezone
from .utils import parse_page


class Url(models.Model):
    original_url = models.URLField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="")
    clicks = models.IntegerField(default=0)
    short_url = models.CharField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse("url_detail", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("url_delete", kwargs={"pk": self.id})

    def get_short_url(self):
        short_url = self.short_url.split("/")[-1]
        return reverse("find_original_url", kwargs={"short_url": short_url})

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        return "{} : {}".format(self.original_url, self.short_url)


@receiver(pre_save, sender=Url)
def my_callback(sender, instance, *args, **kwargs):
    instance.text = parse_page(instance.original_url)
