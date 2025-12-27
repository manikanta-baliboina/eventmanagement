from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('success/', views.success, name='success'),
]
