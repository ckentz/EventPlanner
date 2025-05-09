from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('', views.event_list, name='event_list'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('browse/', views.browse_events, name='browse_events'),

]
