from django.db import models
from django.core.validators import FileExtensionValidator

# Our database variables 
class Customer(models.Model):
    customer_Name=models.CharField(max_length=200)
    customer_Surname=models.CharField(max_length=200)
    customer_Date_of_birth=models.CharField(max_length=200)
    customer_Financial_Excel=models.FileField(null=True, blank=False, validators=[FileExtensionValidator(['xlsx'])])


    class Meta:
        db_table='customer'
