from django.urls import path
from postalk import views

urlpatterns = [
    path('', views.hello_postalk, name='hello_postalk'),
]
