from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barbers/', views.barbers_index, name='index'),
    path('barbers/<int:barber_id>', views.barbers_detail, name='detail'),
    path('barbers/create/', views.BarberCreate.as_view(), name='barbers-create'),
    path('barbers/<int:pk>/update', views.BarberUpdate.as_view(), name='barbers_update'),
    path('barbers/<int:pk>/delete', views.BarberDelete.as_view(), name='barbers_delete'),
    path('barbers/<int:barber_id>/add_appointment', views.add_appointment, name='add_appointment')
]