from django.contrib import admin
from . import models

# Register your models here.

#registering the author model to the admin
@admin.register(models.Author)
class Author(admin.ModelAdmin):
    list_display = ['description', 'location', 'image']
