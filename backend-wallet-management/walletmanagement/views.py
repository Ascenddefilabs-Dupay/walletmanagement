# walletmanagement/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserPassword
from .serializers import UserPasswordSerializer
import random
import string
import hashlib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RecoveryPhrase

@api_view(['POST'])
def save_password(request):
    if request.method == 'POST':
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password saved successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def recovery_phrase(request):
    if request.method == 'GET':
        # Generate a random word list
        words = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(100)]
        shuffled = random.sample(words, 12)
        phrase = ' '.join(shuffled)
        return Response({'phrase': phrase})

    elif request.method == 'POST':
        # Save the provided phrase to the database
        phrase = request.data.get('phrase')
        if phrase:
            # Hash the phrase
            hashed_phrase = hashlib.sha256(phrase.encode()).hexdigest()
            RecoveryPhrase.objects.create(phrase=hashed_phrase)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error', 'message': 'Phrase not provided'}, status=400)