from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
TIME = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening')
)

SKILLS = (
    ('H', 'Hair-Cut'),
    ('C', 'Hair-Color'),
    ('N', 'Nail')
)
class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})


class Barber(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()
    description = models.TextField(max_length=250)
    locations = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'barber_id' : self.id})

class Schedule(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=TIME,
        default=TIME[0][0]
    )
    skill = models.CharField(
        max_length=1,
        choices=SKILLS,
        default=SKILLS[0][0]
        )
    customer = models.CharField(max_length=50)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_skill_display()} on {self.date} in {self.get_time_display()}"
    class Meta:
        ordering = ['-date']
    
