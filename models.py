from django.db import models
class mstdata(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=12)
    gender=models.CharField(max_length=40)
    dob = models.DateField()
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    role=models.CharField(max_length=30)

