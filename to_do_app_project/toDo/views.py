from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout , authenticate
# Create your views here.

def home(request):
    return render(request,'toDo/home.html')
    
def signUpUser(request):
    if request.method == "GET":
        return render(request,'toDo/signupuser.html',{'form':UserCreationForm()})
    else :
        # create a new user 
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                #if user name mtach one exisit
                return render(request,'toDo/signupuser.html',{'form':UserCreationForm(),'error':"The user name has already been taken. Please choose a new user name"})

                
        else:
            #if passwords didint match
            return render(request,'toDo/signupuser.html',{'form':UserCreationForm(),'error':"Passwords did not match"})
        
        
def currenttodos(request):
    return render(request, 'toDo/currenttodos.html')
     
def logInUser(request):
    if request.method == "GET":
        return render(request, 'toDo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'] , password=request.POST['password'])
        if user is None :
            return render(request, 'toDo/loginuser.html', {'form': AuthenticationForm(), 'error': "User and password did not match"})

        else :
            login(request,user)
            return redirect('currenttodos')
             
        
       

   
         
def logOutUser(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')
