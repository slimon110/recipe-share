from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)
    description = models.TextField()
