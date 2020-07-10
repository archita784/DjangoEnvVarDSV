

# Create your views here.
from django.shortcuts import render,redirect,reverse
import datetime
from .models import Feedback,Registration,Login
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def contactus(request):
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def feed(request):
    name = request.POST['name']
    emailaddress = request.POST['emailaddress']
    telephone = request.POST['telephone']
    subject = request.POST['subject']
    message = request.POST['message']
    ci = Feedback(name=name,emailaddress=emailaddress,telephone=telephone,subject=subject, message=message)
    ci.save()
    return redirect('index')
def custreg(request):
    username=request.POST['username']
    emailaddress = request.POST['emailaddress']
    password=request.POST['password']
    li = Registration(username=username,emailaddress=emailaddress, password=password)
    li.save()
    ai = Login(userid=emailaddress, password=password)
    ai.save()
    return render(request, 'registration.html',)

def validateuser(request):
   userid=request.POST['userid']
   password=request.POST['password']
   try:
       V=Login.objects.get(userid=userid,password=password)
       if V is not None:
           return redirect(reverse('userzone:userhome'))
   except ObjectDoesNotExist:
           return redirect(reverse('login'))


