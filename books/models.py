from django.db import models

from authors.models import Author
# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name="Book Name", null=False, blank=False, max_length=128)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)