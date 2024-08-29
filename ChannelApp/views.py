from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from django.shortcuts import render
@api_view(["POST"])
def loginView(request, *args, **kwargs):
    username = request.data.get("username")
    password = request.data.get("password")
    
    # Authenticate the user
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({
            "user_not_found": "There is no user with this username and password!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Get or create a token for the user
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        "token": token.key,
    }, status=status.HTTP_200_OK)


def index(request):
    return render(request,'index.html')