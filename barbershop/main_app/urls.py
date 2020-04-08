from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barbers/', views.barbers_index, name='index')
]