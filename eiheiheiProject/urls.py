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
from colum_app import views as colum_app_views
from sign_app import views as sign_app_views

urlpatterns = [
    #main_app
    #path('test/',main_app_views.test,name='test'),
    #path('admin/', admin.site.urls),
    path('',main_app_views.JumpToMainPage,name='JumpToMainPage'),
    path('MainPage',main_app_views.MainPage,name='MainPage'),
    path('Ops_GreenShit',main_app_views.GreenShitOps,name='GreenShitOps'),

    #colum_app
    path('ColumnPage_primary',colum_app_views.Primary,name='Primary'),
    path('ColumnPage_middle',colum_app_views.Middle,name='Middle'),
    path('ColumnPage_high',colum_app_views.High,name='High'),
    path('ColumnPage_university',colum_app_views.University,name='university'),

    #log_app
    path('SignIn',sign_app_views.sign_in,name='sign_in'),
    path('SignUp',sign_app_views.sign_up,name='sign_up'),
    path('SignOut',sign_app_views.sign_out,name='sign_out'),
]

# handeler404='main_app_views.GreenShitOps'