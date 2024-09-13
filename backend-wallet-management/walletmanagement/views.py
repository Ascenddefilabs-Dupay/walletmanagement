import hashlib
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import WalletData, CustomUser
from .serializers import WalletDataSerializer,CustomUserSerializer
from django.utils import timezone

@api_view(['POST'])
def save_wallet_data(request):
    print(request)
    # Deserialize the JSON data to Python data
    serializer = WalletDataSerializer(data=request.data)

    # Validate and save the data if valid
    if serializer.is_valid():
        wallet_data = serializer.save()

        # Assign 'created' status to the wallet's creation state
        wallet_data.creation_state = 'created'
        wallet_data.save()

        user_id = request.data.get('user_id')  # Get user_id from request data
        if user_id:
            try:
                # Fetch the user with the given user_id
                user = CustomUser.objects.get(user_id=user_id)
                user.registration_status = True  # Update the registration_status
                user.save()  # Save the updated user record
            except CustomUser.DoesNotExist:
                # Return an error response if the user is not found
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({'message': 'Wallet data saved successfully'}, status=status.HTTP_201_CREATED)
    
    # Return an error response if the data is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def check_recovery_phrase(request):
    phrases = request.data.get('phrases', [])
    print(request.data)
    print(phrases)
    if len(phrases) != 12:
        return Response({"success": False, "message": "Invalid number of words."}, status=400)

    # Join the phrases into a single string
    phrase_string = ' '.join(phrases)

    # Convert to the hash format (SHA-256)
    # hashed_phrase = hashlib.sha256(phrase_string.encode()).hexdigest()
    wallet = WalletData.objects.filter(recovery_phrases=phrase_string).first()
    # Check if the hashed phrase exists in the database
    if wallet:
        print(wallet.wallet_id)
        return Response({"success": True, "wallet_id": wallet.wallet_id})
    else:
        return Response({"success": False, "message": "Recovery phrase is incorrect."})
    

@api_view(['POST'])
def update_password(request):
    wallet_id = request.data.get('wallet_id')
    new_password = request.data.get('password')

    if not wallet_id or not new_password:
        return Response({"success": False, "message": "wallet_id and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        wallet = WalletData.objects.get(wallet_id=wallet_id)
        wallet.password = new_password
        wallet.save()
        return Response({"success": True, "message": "Password updated successfully"}, status=status.HTTP_200_OK)
    except WalletData.DoesNotExist:
        return Response({"success": False, "message": "Wallet ID not found"}, status=status.HTTP_404_NOT_FOUND)
    

def get_latest_wallet_id(request):
    latest_wallet = WalletData.objects.latest('created_at')
    wallet_id = latest_wallet.wallet_id if latest_wallet else None
    return JsonResponse({'wallet_id': wallet_id})

@api_view(['GET'])
def get_user_data(request, user_id):
    try:
        # Query the CustomUser model based on user_id
        user = CustomUser.objects.get(user_id=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)