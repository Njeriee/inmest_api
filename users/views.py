from django.shortcuts import render
from inmest_api.utilities import generate_400_response, generate_unique_code

from users.serializers import AuthSerializer, UserSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from django.db.models import Q
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
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
        temporal_login = IMUser.objects.get(temporal_login)
        temporal_login += 1
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
        return generate_400_response("Invalid username or password")


# class based API view
class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        # the process
        #1. receiving the username in this case an email
        username = request.data.get("username")
        if not username :
            return generate_400_response("invalid username")
        #2. check if the user exists and generate otp
        try:
            user = IMUser.objects.get(username=username)
            otp_code = generate_unique_code()
        except:
            return generate_400_response("user does not exist")
        #3. send OTP code
        user.unique_code = otp_code
        user.save()
        #4. repond to the user
        return Response({"detail":"Please check your email for an OTP code"},status.HTTP_200_OK)

# create a reset password api view
class ResetPasswordAPIView(APIView):
    # implement a post request to do the following
    # 1.Receive the following info (username, unique code and new_password) as reqyest payload
    def post(self,request,*args,**kwargs):
        username = request.data.get("username")
        unique_code = request.data.get("unique_code")
        new_password = request.data.get("new_password")

    # 2.Validate the inputs sent(username ,unique code and new_password)
        if not username or unique_code or new_password:
            Response({"detail":"invalid credentials"},status.HTTP_400_BAD_REQUEST)
    # 3.Check the existance of the user and the unique code
        
    # 4.if the user exists update the user password to be the new password
    pass

class CurrentUserProfile(APIView):
    def get(self,request,*args,**kwargs):
        user = UserSerializer(request.user,)
        return Response({'results':user.data})
    

class ChangePassword(APIView):
    def post (self,request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        username = request.user.username

        if old_password is None:
            return Response({'detail':"please provide old password"},status.HTTP_400_BAD_REQUEST)
        
        if new_password is None:
            return Response({'detail':"please provide new password"},status.HTTP_400_BAD_REQUEST)
        
        if old_password == new_password:
            return Response({'detail':"new password cannot be the same as old password"})