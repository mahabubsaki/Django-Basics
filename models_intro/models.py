from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.TextField(default="")
    
    # def __str__(self) -> str:
    #     return f"Rolle : {self.roll} - Name : {self.name}"
    


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    f_name = models.CharField(max_length=30)
    address = models.TextField()