# walletmanagement/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserPassword
from .serializers import UserPasswordSerializer

@api_view(['POST'])
def save_password(request):
    if request.method == 'POST':
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password saved successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
