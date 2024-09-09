from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from . models import *

def RegisterPage(request):
    return render(request,"app/register.html")

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def UserRegister(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Confirm_Password = request.POST.get('cpassword')

        if User.objects.filter(email=Email).exists():
            message = "User already exists"
            return render(request, "app/login.html", {'msg': message})

        if Password != Confirm_Password:
            message = "Password and Confirm Password do not match"
            return render(request, "app/register.html", {'msg': message})

        user = User.objects.create_user(username=Username, email=Email, password=Password)
        message = "User registered successfully"
        return render(request, "app/login.html", {'msg': message})

    return redirect('registerpage')
# def index(request):
#     return render(request, 'index.html')

def login(request):
    return render(request,"app/login.html")

def loginuser(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['password']

        users = User.objects.filter(Username=Username)
        if not users.exists():
            message = "User does not exist"
            return render(request, "app/login.html", {'msg': message})

        user = users.first()  # Get the first user object from the QuerySet
        if user.Password == Password:
            request.session['Username'] = user.Username
            request.session['Email'] = user.Email
            return render(request, "app/home.html")
        else:
            message = "Password does not match"
            return render(request, "app/login.html", {'msg': message})
    else:
        return HttpResponse("Invalid request method", status=405)
def home(request):
    return render(request, "app/home.html")
def map(request):
    return render(request,"app/map.html")


