from django.shortcuts import render
from . forms import demo_form

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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request,"./contact/index.html",{'email':email,'password':password})
    return render(request,"./contact/index.html")
def faq(request):
    return render(request,"./faq/index.html")
def djform(request):
    if request.method == 'POST':
    # get the data from form
        form = demo_form(request.POST,request.FILES)
        if form.is_valid():
        # we will get the form data here as dictionary
            file = form.cleaned_data['file']
            print(file)
            with open('./home/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return render(request,"./dj-form/index.html",{'form':form})
    else:
        form = demo_form()
        return render(request,"./dj-form/index.html",{'form':form})