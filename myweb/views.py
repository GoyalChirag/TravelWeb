from django.shortcuts import redirect, render
from .models import Destination
from django.contrib.auth.models import User,auth


def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests': dests})

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
        user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request,'register.html')