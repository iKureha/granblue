from django.db import models

class Boss(models.Model):
    name = models.CharField(max_length=15)
    level = models.IntegerField()
    code = models.CharField(max_length=8)


