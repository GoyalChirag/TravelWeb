from django.shortcuts import redirect, render
from .models import Destination
from django.contrib.auth.models import User,auth
from django.contrib import messages


def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests': dests})

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('user does not exist')
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        # birthday = request.POST['birthday']
        email = request.POST['email']
        # phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('Password do not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')