from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^userhome',views.userhome,name='userhome'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^signing', views.signing, name='signing'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^verification', views.verification, name='verification'),

]