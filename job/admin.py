from django.contrib import admin

# Register your models here.
from .models import Job , Category

admin.site.register(Job) #add Jon on admin control
admin.site.register(Category)