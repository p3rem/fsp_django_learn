from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    phno=models.IntegerField()
    age=models.IntegerField()
    class Meta:
        db_table="user"

class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    pincode=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    phno=models.IntegerField()
    emailid=models.EmailField()
    adhaar_no=models.IntegerField()
    class Meta:
        db_table="student"

class picfile(models.Model):
    fname=models.CharField(max_length=50)
    furl=models.ImageField()
    class Meta:
        db_table='picfile'