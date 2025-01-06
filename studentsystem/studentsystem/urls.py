"""
URL configuration for studentsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from studentapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('register/',register,name="register"),
    path('teacherreg/',teacher_register,name="teacher_register"),
    path('logins/',logins,name="logins"),
    path('admins/',admins,name="admins"),
    
    path("viewteacher/",viewteacher,name="viewteacher"),
    path("deleteteacher/",deleteteacher,name="deleteteacher"),
    path("delteacher/<int:id>/",delteacher,name="delteacher"),
    path("viewstudent/",viewstudent,name="viewstudent"),
    path("approvestudent/",approvestudent,name="approvestudent"),
    path("approve/<int:id>/",approve,name="approve"),
    path("deletestudent/",deletestudent,name="deletestudent"),
    path("delstudent/<int:id>/",delstudent,name='delstudent'),
    
    path("studenthome/",studenthome,name="studenthome"),
    path("editstudent/",editstudent,name='editstudent'),
    path("updatestudent/<int:id>",updatestudent,name="updatestudent"),
    path("logoutstudent/",logoutstudent,name="logoutstudent"),
    path("hometeacher",hometeacher,name="hometeacher"),
    
    path("teacherhome/",teacherhome,name='teacherhome'),
    path("editteacher/",editteacher,name="editteacher"),
    path("updateteacher/<int:id>/",updateteacher,name="updateteacher"),
    path("logoutteacher/",logoutteacher,name='logoutteacher'),
    path("index/",index,name='index'),

]
