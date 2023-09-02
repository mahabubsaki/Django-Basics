from django.contrib import admin
from . import models
from models_intro.models import StudentModel
from book.models import BookStoreModel
# Register your models here to see on admin panel
admin.site.register(models.Student)
admin.site.register(StudentModel)
