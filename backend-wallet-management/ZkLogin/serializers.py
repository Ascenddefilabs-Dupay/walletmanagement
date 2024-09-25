from rest_framework import serializers
from walletmanagement.models import WalletData

class ZkLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletData
        fields = ['sui_address','balance','wallet_id','user_id']  