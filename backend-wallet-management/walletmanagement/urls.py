# walletmanagement/urls.py
from django.urls import path
from .views import save_password  # Correct import
from .views import recovery_phrase

urlpatterns = [
    path('api/password/', save_password, name='save_password'),
    path('api/recovery-phrase/', recovery_phrase, name='recovery-phrase'),
]
