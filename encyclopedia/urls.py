from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.save, name="save"),
    path("random", views.random_page, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),        
    path("<str:title>", views.page, name="page")    
]
