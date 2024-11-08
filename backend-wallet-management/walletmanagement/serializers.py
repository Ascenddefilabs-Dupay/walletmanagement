# # walletmanagement/serializers.py
# from rest_framework import serializers
# from .models import CryptoWallet  # Correct import

# class UserPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CryptoWallet
#         fields = ['password']

# class RecoveryPhraseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CryptoWallet
#         fields = ['phrase']

# serializers.py
# serializers.py
from rest_framework import serializers
from .models import WalletData,CustomUser

class WalletDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletData
        fields = ['wallet_id', 'password', 'recovery_phrases', 'created_at', 'user_id']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_email', 'user_first_name', 'user_last_name', 'user_dob', 'user_phone_number', 'user_country', 'user_city', 'user_address_line_1', 'user_state','user_address_line_2','user_pin_code']

# class RecoveryPhraseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WalletData
#         fields = ['recovery_phrases']