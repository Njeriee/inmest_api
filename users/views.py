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


class ResetPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
      
        unique_code = request.data.get('unique_code')
        new_password = request.data.get('new_password')
        username = request.data.get('username')

        if not unique_code:
            return generate_400_response("Unique Code is required")
        if username == None or username == "":
            return generate_400_response("Email is required")
        if new_password is None:
            return generate_400_response("Provide password")

        try:
            myuser = IMUser.objects.get(unique_code=unique_code, username=username)
            myuser.unique_code = ""
            myuser.temporal_login_fails = 0
            myuser.permanent_login_fails = 0
            myuser.set_password(new_password)
            myuser.is_active = True
            myuser.is_blocked = False
            myuser.save()

            user = AuthSerializer(myuser, context={'request': request})
            return Response({'results': user.data, 'response_code': '100'}, status=200)

        except IMUser.DoesNotExist:
            return Response({'detail': "Invalid OTP Code", 'response_code': '101'}, status=400)   



class CurrentUserProfile(APIView):

    def get(self, request, *args, **kwargs):
        """
        Fetches a user's profile
        """
        user = UserSerializer(request.user, many=False, context={'request': request})
        return Response({'results': user.data, 'response_code': '100'}, status=200)

    def put(self, request, *args, **kwargs):
        """
        Updates a user's profile

        """
        user = request.user
        first_name = request.data.get("first_name")
        profile = request.data
        # profile.profile_picture = request.data.get("user_avatar")

        try:
            serializer = UserSerializer(user, context={'request': request}, data=profile, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'results': serializer.data, 'response_code': '100'}, status=200)
            return Response({'results': serializer.errors, 'response_code': '101'}, status=400)
        except:
            serializer = UserSerializer(user, context={'request': request}, data=profile, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'results': serializer.data, 'response_code': '100'}, status=200)
            serializer = UserSerializer(profile, context={'request': request})
            return Response({'detail': serializer.errors, 'response_code': '100'}, status=400)
    
class ChangePassword(APIView):
    """
    Change password if logged in   
    """

    def post(self, request, *args, **kwargs):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        username = request.user.username
        if old_password is None:
            return Response({'detail': "Please provide old password", 'response_code': '101'},
                            status=400)
        if new_password is None:
            return Response({'detail': "Please provide new password", 'response_code': '101'},
                            status=400)
        if old_password == new_password:
            return Response({'detail': "Old and new passwords must not be same", 'response_code': '101'},
                            status=400)

        user = authenticate(username=username, password=old_password)

        if user is not None:
            myuser = request.user
            myuser.set_password(new_password)
            myuser.save()

            user = UserSerializer(myuser, context={'request': request})
            return Response({'results': user.data, 'response_code': '100'}, status=200)
        else:
            return Response({'detail': "Your old password is incorrect", 'response_code': '101'},
                            status=400)