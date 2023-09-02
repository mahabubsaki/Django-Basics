from django.shortcuts import render,redirect
from . import models
from models_intro.forms import StudentForm

# Create your views here.
def home(request):
    students = models.Student.objects.all()
    return render(request,"home.html",context={'data':students})

def delete_student(request,roll):
    std = models.Student.objects.get(pk = roll).delete()
    print(std)
    return redirect("home")

def model_form(request):
    std = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            
    return render(request,"form.html",{'form':std})