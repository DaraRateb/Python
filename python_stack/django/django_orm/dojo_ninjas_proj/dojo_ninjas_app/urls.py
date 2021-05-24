from django.urls import path
from django.urls import URLPattern
from . import views

urlpatterns=[
    path('',views.index),
    path('adddojo',views.adddojo),
    path('addninja',views.addninja),
]