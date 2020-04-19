from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barbers/', views.barbers_index, name='index'),
    path('barbers/<int:barber_id>', views.barbers_detail, name='detail'),
    path('barbers/create/', views.BarberCreate.as_view(), name='barbers-create'),
    path('barbers/<int:pk>/update', views.BarberUpdate.as_view(), name='barbers_update'),
    path('barbers/<int:pk>/delete', views.BarberDelete.as_view(), name='barbers_delete'),
    path('barbers/<int:barber_id>/add_appointment', views.add_appointment, name='add_appointment'),
    path('locations/', views.Locations.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:pk>/update/',views.LocationUpdate.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
    path('barber/<int:barber_id>/new_location/<int:location_id>', views.new_location, name='new_location'),
]