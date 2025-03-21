from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import company_list, edit_company , add_company , delete_company

urlpatterns = [
    path('company/list/', company_list, name='company_list'),
    path('company/add/', add_company, name='add_company'),
    path('company/edit/<int:company_id>/', edit_company, name='edit_company'),
    path('company/delete/<int:company_id>/', delete_company, name='delete_company'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)