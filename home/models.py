from django.db import models

# Create your models here.


class book(models.Model):
    firstname: models.CharField(max_length=30)
    lastname: models.CharField(max_length=30)
    number: models.IntegerField()
