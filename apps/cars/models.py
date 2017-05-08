from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=40)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class CarUser(models.Model):
    userid = models.ForeignKey(User)
    carid =  models.ForeignKey(Car)

    def __str__(self):
        return self.userid.username
