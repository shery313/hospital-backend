from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,blank=True,null=True)
    phone=models.IntegerField()
    date=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    time=models.TimeField(auto_now_add=False,null=True,blank=True)
    patient=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    doctor=models.ForeignKey('Docter',on_delete=models.CASCADE,null=True,blank=True)

    # def __str__(self):
    #     return str(self.doctor)
class Docter(models.Model):
    name=models.CharField(max_length=200)
    image=models.FileField(default='docter.jpg',upload_to='media/doctors',null=True,blank=True)
    specialty=models.CharField(max_length=200,null=True,blank=True)
    experience=models.CharField(max_length=200,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    education=models.CharField(max_length=600,null=True,blank=True)
    rating=models.IntegerField(default=0,null=True)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.name

