from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Home Page Route
    path('dashboard',home, name = 'dashboard' )
]
