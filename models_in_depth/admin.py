from django.contrib import admin
from models_in_depth.models import CommonInfoClass,EmployeeClass,Person,Post,Passport,Student,Teacher
# Register your models here.
# we cant register abstract classes
# admin.site.register(CommonInfoClass)


# for visualize the model into table
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author','category','first_pub','last_pub')
    
admin.site.register(EmployeeClass,EmployeeModelAdmin)

@admin.register(Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']
@admin.register(Passport)
class PassportModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','pass_num','page','validity']
    
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','post_cap','post_details']
    
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','class_name','validity']
    
@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id','student','name','subject','mobile_no']
    
    
admin.site.register(Student)
admin.site.register(Teacher)