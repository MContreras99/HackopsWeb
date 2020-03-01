from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hackops-home'),
    path('about/', views.about, name='hackops-about'),
]
