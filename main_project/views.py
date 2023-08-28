from django.http import HttpResponse as res

def homePage(request):
  return res("<h1>Hello</h1>")

def newHomePage(request):
    return res("Hello2")