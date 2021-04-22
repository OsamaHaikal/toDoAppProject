"""to_do_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from toDo import views

urlpatterns = [
    path('',views.home , name='home'),
    
    path('admin/', admin.site.urls),
    # Auth 
    path('signup/',views.signUpUser , name='signupuser'),  
    path('logout/',views.logOutUser , name='logoutuser'),
    path('login/', views.logInUser, name='loginuser'),

    #to dos
    path('create/',views.createToDo , name='createtodo'),
    path('current/',views.currenttodos , name='currenttodos'),
    path('todo/<int:todo_pk>/',views.viewtodo , name='viewtodo')



]
