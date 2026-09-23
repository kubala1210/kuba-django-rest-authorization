from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class MyPayloadView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        token_data = request.auth

        return Response({'token_payload': token_data.payload})

# Create your views here.
