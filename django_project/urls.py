
from django.contrib import admin
from django.urls import path
from appdogui import views

urlpatterns = [
  path('', views.home),
  path('admin/', admin.site.urls),
  path('add-band/', views.add_band, name='add_band'),
  path('add-music/', views.add_music, name='add_music'),
  path('add-instrument/', views.add_instrument, name='add_instrument'),
  path('remove-music/', views.remove_music, name='remove_music'),
  path('remove-band/', views.remove_band, name='remove_band'),
  path('remove-instrument/', views.remove_instrument, name='remove_instrument'),
  path('edit-instrument/<int:instrument_id>/', views.edit_instrument, name='edit_instrument'),
  path('edit-music/<int:music_id>/', views.edit_music, name='edit_music'),
  
]
