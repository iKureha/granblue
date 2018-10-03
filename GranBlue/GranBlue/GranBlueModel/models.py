from django.db import models

# Create your models here.

class Granblue(models.Model):
    name = models.CharField(max_length=15)
    level = models.IntegerField()
    code = models.CharField(max_length=8)


