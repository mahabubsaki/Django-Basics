from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request,"./root/index.html")
def about(request):
    return render(request,"./about/index.html",{'name':'Saki Mahabub'})
def services(request):
    return render(request,"./services/index.html")
def blogs(request):
    return render(request,"./blogs/index.html")
def contactus(request):
    return render(request,"./contact/index.html")
def faq(request):
    return render(request,"./faq/index.html")