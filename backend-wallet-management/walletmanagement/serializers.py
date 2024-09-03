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
from .models import WalletData

class WalletDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletData
        fields = ['wallet_id', 'password', 'recovery_phrases', 'created_at', 'user_id']

# class RecoveryPhraseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WalletData
#         fields = ['recovery_phrases']
