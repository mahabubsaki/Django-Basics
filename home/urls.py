from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about-us/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('blogs/',views.blogs,name="blogs"),
    path('contact-us/',views.contactus,name="contact"),
    path('faq/',views.faq,name="faq"),
]