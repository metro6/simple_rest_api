from django.db import models

from authors.models import Author
# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name="Book Name", null=False, blank=False, max_length=128)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural= 'Books'

    def __str__(self):
        return self.name + '; ' + self.author.name