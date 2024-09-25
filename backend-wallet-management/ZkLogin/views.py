from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from walletmanagement.models import WalletData
from .serializers import ZkLoginSerializer
from django.http import JsonResponse
import logging

# Create your views here.
# @api_view(['POST'])
# def save_account(request):
#     serializer = ZkLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

logger = logging.getLogger(__name__)

@api_view(['POST'])
def save_account(request):
    serializer = ZkLoginSerializer(data=request.data)
    print(serializer)
    # Validate the incoming data
    if serializer.is_valid():
        try:
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Log the error for debugging
            logger.error(f"Error saving wallet account: {e}")
            return Response({"error": "An error occurred while saving the account."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Return 400 status with error messages if data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_latest_wallet_id(request):
    latest_wallet = WalletData.objects.latest('created_at')
    wallet_id = latest_wallet.wallet_id if latest_wallet else None
    print(wallet_id)
    return JsonResponse({'wallet_id': wallet_id})
