from rest_framework.response import Response
from rest_framework import status

def generate_400_response(message):
    return Response({"detail":message},status.HTTP_400_BAD_REQUEST)