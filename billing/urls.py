# billing/urls.py
from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
]
