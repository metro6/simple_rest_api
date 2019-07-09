from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name="Author", null=False, blank=False, unique=True, max_length=128)