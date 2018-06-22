"""eiheiheiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from main_app import views as main_app_views

urlpatterns = [
    path('test/',main_app_views.test,name='test'),
    path('admin/', admin.site.urls),
    path('',main_app_views.JumpToMainPage,name='JumpToMainPage'),
    path('MainPage',main_app_views.MainPage,name='MainPage'),
]
