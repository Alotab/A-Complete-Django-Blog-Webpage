from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'author', 'image', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}
    # date_hierarchy = ['publish']
    # ordering = ['status', 'publish']