from django.http import HttpResponse as res
from django.shortcuts import render

#send response via template render
def homePage(request):
  # We can send dynamic values in our html file to render them
  return render(request,"./root/index.html",context={"name":"Mahabub Saki",'age':20,"cars":[{'name':'tyoyata','year':2},{'name':'maruti','year':1},{'name':'mitsubishi','year':69}]})

#send response via httpresponse
def homePage2(request):
  return res("<h1>hi</h1>")
