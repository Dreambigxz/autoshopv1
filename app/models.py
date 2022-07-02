from django.db import models
from django.utils import timezone
from craigslistworker.domain import which_city
import  uuid
from django.urls import reverse
import modules
# Create your models here.

class Filter(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.tags}'

class Car(models.Model):

    CITY_CATEGORIES = which_city()

    all_sf_bayAreas =   {

                "eby": "east bay",
                "nby": "north bay",
                "pen": "peninsula",
                "sfc": "san francisco",
                "scz": "santa cruz",
                "sby": "south bay",
    }

    AREA_CATEGORIES = [
    ("eby", "east bay"),
    ("nby", "north bay"),
    ("pen", "peninsula"),
    ("sfc",  "san francisco"),
    ("scz", "santa cruz"),
    ("sby", "south bay"),
    ]

    which_city = models.CharField(max_length=50, default='minneapolis', choices=CITY_CATEGORIES)
    which_area = models.CharField(max_length=50, null=True, blank=True, choices=AREA_CATEGORIES)
    title = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price_string = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    post_url = models.CharField(max_length=200, null=True)
    image = models.ImageField( blank=True)
    datetime = models.DateTimeField(default=timezone.now)
    post_id = models.CharField(max_length=50, null=True, blank=True)
    thumbnails = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    vehicle_options = models.TextField(blank=True)
    location = models.CharField(max_length=80, null=True)
    map_url = models.CharField(max_length=80, null=True)
    display_odometer = models.CharField(max_length=80, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
    def first_image(self):
        image = modules.decode(self.thumbnails)
        try:
            image = image['0']
        except Exception as e:
            image = "static/carimagedefault/default.jpg"
        # if image.url is None:
        #     image = image['1']
        return image

    ordering = ['-datetime']
