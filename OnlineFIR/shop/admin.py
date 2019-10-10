from django.contrib import admin

# Register your models here.
from .models import userdata,fir

admin.site.register(userdata)
admin.site.register(fir)