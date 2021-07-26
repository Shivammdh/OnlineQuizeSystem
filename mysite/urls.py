
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path(r'^admin/login/?$', admin.site.urls),
    path('', include('authenticate.urls')),
]
