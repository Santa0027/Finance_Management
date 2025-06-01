from django.urls import path
from . import views

app_name = "company"

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('add/', views.company_add, name='company_add'),
    path('edit/<int:id>/', views.company_edit, name='company_edit'),
    path('delete/<int:id>/', views.company_delete, name='company_delete'),
    path('individual/add/', views.individual_add, name='individual_add'),
    path('individual/edit/<int:id>/', views.individual_edit, name='individual_edit'),
    path('individual/delete/<int:id>/', views.individual_delete, name='individual_delete'),
]
