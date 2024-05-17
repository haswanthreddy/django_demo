from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.index, name="post index"),
    path("", views.welcome)
]