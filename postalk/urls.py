from django.urls import path
from postalk import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]