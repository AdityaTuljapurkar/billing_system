from django.db import models

# Create your models here.
class Employee_Data(models.Model):
    EmployeeId = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Customer_Data(models.Model):
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length=15)
    total_Bill = models.FloatField()
    Bill_time = models.DateTimeField(auto_now_add=True)