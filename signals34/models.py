from django.db import models
import uuid
# Create your models here.

class CitiesTOScrab(models.Model):
    cities = models.TextField(blank=True)
    looped = models.TextField(blank=True)
    is_lock = models.BooleanField(default=False)


class CrawlerAgent(models.Model):
    user = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=False)
    last_work = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    my_city = models.ForeignKey(CitiesTOScrab, on_delete=models.CASCADE, null=True)
