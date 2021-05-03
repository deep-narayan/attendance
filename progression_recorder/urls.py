"""progression_recorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name='progression_recorder'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register,name='register'),
    path('login/',views.login_call,name='login'),
    path('logout/',views.logout_call,name='logout'),
    path('addsub/',views.addsub,name='addsub'),
    path('viewsub/',views.viewsub,name='viewsub'),
    path('addres/',views.addres,name='addres'),
    path('usd/',views.usd,name='usd'),

]
