from django.shortcuts import render

from users.serializers import AuthSerializer, UserSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from django.db.models import Q
from django.contrib.auth import authenticate, login
# from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.decorators import api_view, permission_classes, action

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")

    new_user = IMUser.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
        )
    
    new_user.set_password(password)
    new_user.save()
    # new_user.generate_auth_token()
    serializer = AuthSerializer(new_user, many=False)
    return Response({"message": "Account successfully created yay!", "result": serializer.data})

# update the login function to check if a user is active,if false tell the user their account is inactive
# check if the user is blocked,if a user login attempt fails increace the temproral login value by 1
# login function
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    # you need the following steps
    # 1. Receive inputs/data from client and validate inputs
    username = request.data.get("username")
    password = request.data.get("password")

    # validate input
    if not username or password:
        Response({"message":"send details bruh"},status.HTTP_400_BAD_REQUEST)
    
    # 2. Check user existance
    try:
        user = IMUser.objects.get(username=username)
    except IMUser.DoesNotExist:
        return Response({"detail":"username does not exist"})
    
    # 3. User authentication
    auth_user = authenticate(username=username,password=password)
    if auth_user:
        login(username,password)
        serializer = UserSerializer
    else:
        return Response({"detail":"Invalid username or password"},status.HTTP_400_BAD_REQUEST)

