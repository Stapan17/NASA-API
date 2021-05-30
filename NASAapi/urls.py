from . import views
from django.urls import path

urlpatterns = [
    path('apod/', views.home, name='home')
]
