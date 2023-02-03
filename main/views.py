from django.shortcuts import render,HttpResponse
from .models import item
# Create your views here.

def index(req):
    all = item.objects.all()
    send = {'item' : all}
    return render(req,'index.html',send)

def dishes(req,name):
    itemfilter = item.objects.get(Name=str(name))
    info = {'info':itemfilter,'title':name}
    return render(req,'dishes.html',info)

def contact(req):
    return render(req,'contact.html')

def bookings(req):
    return render(req,'booking.html')