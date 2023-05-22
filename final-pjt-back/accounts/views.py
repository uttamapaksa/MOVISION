# Create your views here.

from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Userdata
from .serializers import UserdataSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def userdata(request, user_id):

    if request.method == 'GET':
        userdata = get_list_or_404(Userdata, user=user_id)
        serializer = UserdataSerializer(userdata, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserdataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            # serializer = UserdataSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def profile_image(request, user_id):
#     if request.method == 'GET':
#         userdata = get_object_or_404(Userdata, pk=user_id)
#         serializer = MovieSerializer(Userdata, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':