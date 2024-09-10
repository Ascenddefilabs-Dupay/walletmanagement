# # walletmanagement/views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # from .models import UserPassword
# from .serializers import UserPasswordSerializer,RecoveryPhraseSerializer
# import random
# import string
# import hashlib
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # from .models import RecoveryPhrase
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import CryptoWallet
# import hashlib

# @api_view(['POST'])
# def save_password(request):
#     if request.method == 'POST':
#         serializer = UserPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Password saved successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def recovery_phrase(request):
#     if request.method == 'GET':
#         # Generate a random word list
#         words = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(100)]
#         shuffled = random.sample(words, 12)
#         phrase = ' '.join(shuffled)
#         return Response({'phrase': phrase})

#     elif request.method == 'POST':
#         # Save the provided phrase to the database
#         phrase = request.data.get('phrase')
#         if phrase:
#             # Hash the phrase
#             hashed_phrase = hashlib.sha256(phrase.encode()).hexdigest()
#             CryptoWallet.objects.create(phrase=hashed_phrase)
#             return Response({'status': 'success'})
#         else:
#             return Response({'status': 'error', 'message': 'Phrase not provided'}, status=400)
        


# @api_view(['POST'])
# def check_recovery_phrase(request):
#     phrases = request.data.get('phrases', [])
#     if len(phrases) != 12:
#         return Response({"success": False, "message": "Invalid number of words."}, status=400)

#     # Join the phrases into a single string
#     phrase_string = ' '.join(phrases)

#     # Convert to the hash format (SHA-256)
#     hashed_phrase = hashlib.sha256(phrase_string.encode()).hexdigest()

#     # Check if the hashed phrase exists in the database
#     if CryptoWallet.objects.filter(phrase=hashed_phrase).exists():
#         return Response({"success": True})
#     else:
#         return Response({"success": False, "message": "Recovery phrase is incorrect."})


# @api_view(['POST'])
# def create_or_update_wallet(request):
#     phrases = request.data.get('phrases')
#     password = request.data.get('password')

#     if phrases:
#         hashed_phrase = hashlib.sha256(' '.join(phrases).encode()).hexdigest()

#         wallet = CryptoWallet.objects.filter(phrase=hashed_phrase).first()

#         if wallet:
#             wallet.password = password
#             wallet.save()
#             return Response({"message": "Wallet updated successfully", "wallet_id": wallet.wallet_id}, status=status.HTTP_200_OK)
#         else:
#             new_wallet = CryptoWallet(phrase=hashed_phrase, password=password)
#             new_wallet.save()
#             return Response({"message": "Wallet created successfully", "wallet_id": new_wallet.wallet_id}, status=status.HTTP_201_CREATED)

#     return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

# views.py
# views.py
import hashlib
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import WalletData
from .serializers import WalletDataSerializer
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