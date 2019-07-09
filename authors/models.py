from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name="Author", null=False, blank=False, unique=True, max_length=128)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name