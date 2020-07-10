from django.shortcuts import render ,redirect
from generalzone.models import Registration,Login

# Create your views here.
def userhome(request):
    return render(request,'userhome.html')
def logout(request):
    return render(request,'login.html')
def signing(request):
    return render(request,'signing.html')
def contact(request):
    return render(request,'contact.html')

def verification(request):
    return render(request,'verification.html')

