from django.shortcuts import render
from django.http import HttpResponse as res

# Create your views here.

def home(request):
    return render(request,"./dashboard/index.html")