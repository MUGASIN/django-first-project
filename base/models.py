
from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField()
    desg=models.CharField()
    sal=models.FloatField()
    gender=models.CharField()



class student(models.Model):
    stuname=models.CharField()
    stuage=models.IntegerField()
    stugernder=models.CharField()
    stusub=models.CharField()
    stumock=models.BooleanField()
    stumarks=models.IntegerField()
    