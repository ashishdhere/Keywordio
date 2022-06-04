"""Keywordiio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('addshow/',views.addshow,name="addshow"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('student/',views.student,name="student"),
    
    path('api/get',views.Book_get,name="BookGet"),
    path('api/post',views.Book_post,name="BookPOST"),
    path('api/put/<str:pk>',views.Book_Put,name="BookPut"),
    path('api/del/<str:pk>',views.Book_delete,name="Bookdelete")
 
]
