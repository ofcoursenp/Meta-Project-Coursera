from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('menu/',views.index,name='menu'),
    path('menu/<str:name>',views.dishes,name='menu'),
    path('bookings',views.bookings,name='menu'),
    path('contact',views.contact,name='menu'),
]   