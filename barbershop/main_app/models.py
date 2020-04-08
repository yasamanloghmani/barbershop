from django.db import models

# Create your models here.

class Barber(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name