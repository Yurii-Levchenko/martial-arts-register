from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.martial_art_detail, name="martial-art-detail"),

]