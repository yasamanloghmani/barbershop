from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barbers/', views.barbers_index, name='index'),
    path('barbers/<int:barber_id>', views.barbers_detail, name='detail'),
]