from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_Name=models.CharField(max_length=200)
    customer_Surname=models.CharField(max_length=200)
    customer_Date_of_birth=models.CharField(max_length=200)
    customer_Financial_Excel=models.FileField()


    class Meta:
        db_table='customer'
