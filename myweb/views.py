from django.shortcuts import render
from .models import Destination


def index(request):
    dest1= Destination()
    dest1.name = 'Mumbai'
    return render(request,'index.html',{'dest1': dest1})