# walletmanagement/urls.py
from django.urls import path
from .views import save_password  # Correct import

urlpatterns = [
    path('api/password/', save_password, name='save_password'),
]
