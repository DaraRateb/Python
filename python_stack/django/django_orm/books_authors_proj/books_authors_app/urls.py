from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('addbook',views.add_book),
    path('author',views.add_author),
    path('bookdetails/<int:id>',views.book_details),
    
]