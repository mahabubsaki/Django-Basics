from django.db import models

# Create your models here.
# abstract class
class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    # for inheriting by other class
    class Meta:
        abstract = True
        
class StudentClass(CommonInfoClass):
    roll = models.IntegerField()

class TeacherClass(CommonInfoClass):
    salary= models.IntegerField()
    
    
#multitable inheritance
#difference between multitable inheritance and abstract inheritance is we can't use abstract class, this class is only for inherting.on the other hand we can inherit multitable class and use them
class EmployeeClass(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    
class ManagerClass(EmployeeClass):
    take_interview = models.BooleanField()
    



#proxy model which allow use to change other models with the dependecy of current model
#here all the changes made in frind class will effect on all the model proxiying it.In this case only me class proxiying it friend class
class Friend(models.Model):
    school = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)



class Me(Friend):
    class Meta:
        proxy = True
        
        

class Person(models.Model):
    name= models.CharField(max_length=30)
    city= models.CharField(max_length=50)
    email= models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
    
#one to one relationship
class Passport(models.Model):
    user  = models.OneToOneField(to=Person,on_delete=models.CASCADE)
    pass_num = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
#one to many relationship
class Post(models.Model):
    user = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)

class Teacher(models.Model):
    student = models.ManyToManyField(Student)
    name= models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile_no = models.IntegerField(max_length=11)