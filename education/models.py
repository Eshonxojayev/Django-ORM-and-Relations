from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)

# Create your models here.
