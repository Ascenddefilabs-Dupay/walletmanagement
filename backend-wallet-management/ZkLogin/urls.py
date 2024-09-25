from django.urls import path
from .views import save_account

urlpatterns = [
    path('zklogin_api/save_account/',save_account, name='save_account'),
]