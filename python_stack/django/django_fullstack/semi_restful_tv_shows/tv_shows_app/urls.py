from django.urls import path 
from . import views

urlpatterns=[
    path('shows',views.index),
    path('shows/new',views.new_show),
    path('shows/add',views.tv_show),
    path('shows/<int:id>',views.show_shows_id),
    path('shows/<int:id>/edit',views.edit_show),
    path('shows/<int:id>/transit', views.tv_show_edit),
    path('shows/<int:id>/destroy',views.destroy)
    # path('shows/<int:id>/edit',views.tv_show_edit),
    
]