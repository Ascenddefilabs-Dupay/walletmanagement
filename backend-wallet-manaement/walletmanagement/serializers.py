# walletmanagement/serializers.py
from rest_framework import serializers
from .models import UserPassword  # Correct import

class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPassword
        fields = ['password']
