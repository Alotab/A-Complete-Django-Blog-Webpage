from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pics')