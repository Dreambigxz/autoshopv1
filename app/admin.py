from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """docstring for CarAdmin."""

    list_display = ('id', 'post_id', 'price', 'price_string', 'datetime', 'post_url', 'which_city')

admin.site.register(Filter)
