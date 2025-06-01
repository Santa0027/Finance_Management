# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.dashboard, name='service'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_service/', views.add_service, name='add_service'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
]