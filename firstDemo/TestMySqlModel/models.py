from django.db import models


# Create your models here.

class Test(models.Model):
    kname = models.CharField(max_length=20)
    kage = models.CharField(max_length=10)
