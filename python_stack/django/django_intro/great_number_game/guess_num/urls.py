from django.urls import path
from . import views

urlpatterns=[
    path('',views.dumnum),
    path('result',views.guess)
]