from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import add_company, edit_company, company_list

urlpatterns = [
    path('company/add/', add_company, name='add_company'),
    path('company/edit/<int:company_id>/', edit_company, name='edit_company'),
    path('company/list/', company_list, name='company_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)