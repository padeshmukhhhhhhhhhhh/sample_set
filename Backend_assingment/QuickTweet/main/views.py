from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.conf import settings 
    

class post_tweet(APIView):
    def post(self, request):
        name=request.data.get("name")
        if name is None:
            return Response({"msg":"please provide name"},status=404)
        api_key = settings.API_KEY
        print(f"a{api_key}")
        return Response({'data':"appa"},status=200)