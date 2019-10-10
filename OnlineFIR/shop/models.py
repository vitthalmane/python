from django.db import models

# Create your models here.
class userdata(models.Model):
    userid = models.AutoField
    fstname = models.CharField(max_length=20)
    lstname = models.CharField(max_length=20)
    password=  models.CharField(max_length=20)
   # creteddate=models.DateField()
    #mobno =models.IntField(max_length=10)
    email = models.CharField(max_length=30)

class fir(models.Model):
    userid = models.AutoField
    img=models.ImageField(upload_to='fir')
    name=models.CharField(max_length=50,default='ddddd')
    addr=models.CharField(max_length=50,default='ddddd')
    firstation=models.CharField(max_length=50,default='ddddd')
    firtype=models.CharField(max_length=50,default='ddddd')
    firdesc=models.CharField(max_length=1000,default='no')


