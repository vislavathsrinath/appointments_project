from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('create/', views.create_appointment, name='create_appointment'),
    path('success/', views.success, name='success'),
]
