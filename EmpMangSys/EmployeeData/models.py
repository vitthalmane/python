from django.db import models

# Create your models here.
class EmpData(models.Model):
    serialNo=models.BigAutoField
    Emp_name=models.CharField(max_length=100)
    Emp_email=models.EmailField(max_length=50)
    Emp_phonNO=models.IntegerField(default=00)
    Emp_dept=models.CharField(max_length=25,default="NA")


