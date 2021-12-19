from django.db import models



class student(models.Model):
    name = models.CharField(max_length=20)
    usn = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
# Create your models here.
