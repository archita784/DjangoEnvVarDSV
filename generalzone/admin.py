from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Registration,Login,Feedback

# Register your models here.
admin.site.register(Registration)
admin.site.register(Login)
admin.site.register(Feedback)
