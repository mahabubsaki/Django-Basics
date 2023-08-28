from django.shortcuts import render

from django.http import HttpResponse as res
# Create your views here.

def about(request):
    return res("about page")
def home(request):
    return res("Home")