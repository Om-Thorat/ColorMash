from django.db import models

# Create your models here.

class colorcombos(models.Model):
    title = models.CharField(max_length=200)
    rating = models.DecimalField(default=400.00000,max_digits=10,decimal_places=5)
    def __str__(self):
        return self.title