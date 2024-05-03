from django.db import models

# Create your models here.
class temp_details(models.Model):
    Name = models.CharField(max_length=20)
    School = models.CharField(max_length=20)
    Place = models.CharField(max_length=20)
    Phone_Number = models.IntegerField(max_length=20)

class temp2_details(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField
    Number = models.IntegerField(max_length=10)
    How_Much = models.IntegerField(max_length=20)
    You_Order = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)