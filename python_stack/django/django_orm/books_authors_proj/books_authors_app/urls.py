from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('book',views.addbook),
    path('author',views.addauthor)
    )
]