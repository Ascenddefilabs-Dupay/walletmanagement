# # walletmanagement/urls.py
# from django.urls import path
# from .views import save_password  # Correct import
# from .views import recovery_phrase,check_recovery_phrase
# from django.urls import path
# from .views import create_or_update_wallet

# urlpatterns = [
#     path('api/password/', save_password, name='save_password'),
#     path('api/recovery-phrase/', recovery_phrase, name='recovery-phrase'),
#     path('api/check-recovery-phrase/', check_recovery_phrase, name='check_recovery_phrase'),
#     path('api/create-or-update-wallet/', create_or_update_wallet, name='create_or_update_wallet'),
# ]

# urls.py
from django.urls import path
from .views import save_wallet_data

urlpatterns = [
    path('api/save-wallet-data/', save_wallet_data, name='save_wallet_data'),
]
