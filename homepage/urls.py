"""POPtest URL Configuration

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
from django.urls import path, include
import homepage.views as views
urlpatterns = [
    path('', views.main, name='main'),
    path('join/', views.join, name="join"),
    path('ID_check', views.ID_check, name="ID_check"),
    path('nick_check', views.nick_check, name="nick_check"),
    path('join_agree', views.join_agree, name="join_agree"),
    path('login/', views.login, name="login"),
    path('cms/', include('cms.urls', namespace='cms')),
    path('logout/', views.logout, name="logout"),
    path('find_id/', views.find_id, name="find_id"),
    path('find_pwd/', views.find_pwd, name="find_pwd"),
    path('pwd_reset/', views.pwd_reset, name="pwd_reset"),    
    path('mypage/', views.myList.as_view(), name="mypage"),
    path('balance/', views.balance, name="balance"),
]
