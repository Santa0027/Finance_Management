from django.urls import path
from .views import (
    create_invoice, save_invoice, delete_invoice,
    add_invoice_item, delete_invoice_item ,billing
)

urlpatterns = [
    path('billing/', billing, name='billing'),
    path('create/', create_invoice, name='create_invoice'),  # Invoice creation page
    path('save/', save_invoice, name='save_invoice'),  # Save new/edit invoice (AJAX)
    path('delete/', delete_invoice, name='delete_invoice'),  # Delete invoice (AJAX)
    path('add_item/', add_invoice_item, name='add_invoice_item'),  # Add invoice item (AJAX)
    path('delete_item/', delete_invoice_item, name='delete_invoice_item'),  # Delete invoice item (AJAX)
]
