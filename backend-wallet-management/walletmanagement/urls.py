from django.urls import path
from .views import save_wallet_data,get_user_data,check_recovery_phrase, update_password, get_latest_wallet_id

urlpatterns = [
    path('walletmanagementapi/save-wallet-data/', save_wallet_data, name='save_wallet_data'),
    path('walletmanagementapi/check-recovery-phrase/', check_recovery_phrase, name='check_recovery_phrase'),
    path('walletmanagementapi/update-password/', update_password, name='update_password'),
    path('walletmanagementapi/latest_wallet_id/', get_latest_wallet_id, name='get_latest_wallet_id'),
    path('walletmanagementapi/user/<str:user_id>/', get_user_data, name='get_user_data'),
]