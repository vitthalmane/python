from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   # path('admin/',admin.site.urls),
    path('',views.index,name="Shophome"),
    path('ecomp/',views.ecomp,name="ecomp"),
    path('getecomp/',views.getecomp,name='getecomp'),
    path('regis/',views.regis,name='regis'),
    path('upload/',views.upload,name='upload'),
    path('store/',views.store,name='store'),
]
