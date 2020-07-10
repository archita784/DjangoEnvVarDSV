from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'login', views.login, name='login'),
    url(r'registration', views.registration, name='registration'),
    url(r'contactus', views.contactus, name='contactus'),
    url(r'aboutus', views.aboutus, name='aboutus'),
    url(r'^feed', views.feed, name='feed'),
    url(r'^custreg', views.custreg, name='custreg'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
    ]