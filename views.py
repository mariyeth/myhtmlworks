from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
          return render(request,'index.html')
def products(request):
        return render(request,'products.html')
def login(request):
        return render(request,'login.html')
def register(request):
        if request.method=="POST":
                username=request.POST['username']
                email=request.POST['email']
                password=request.POST['password']
                if User.objects.filter(username=username).exists():
                        messages.info(request,"Username already exists!")
                        return redirect('register')
                elif User.objects.filter(email=email).exists():
                        messages.info(request,"Email taken!")
                        return redirect('register')
                else:user=User.objects.create_user(username=username,email=email,password=password)
                user.save(); return redirect('/')
        else:
                return render(request,'register.html')
        







