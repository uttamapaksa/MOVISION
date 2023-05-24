# Create your views here.
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


# 모든 유저 데이터 가져오기
@api_view(['GET', 'POST'])
def get_profile(request, user_id):

    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 팔로우, 언팔로우 하기
@api_view(['POST'])
def follow(request, user_id):
    user = request.user
    print(user)
    print(user.pk)
    person = get_object_or_404(User, pk=user_id)
    if user in person.followers.all():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return Response('follow_views.py')


# 프로필 이미지 저장하기
@api_view(['POST'])
def profile_image(request, user_id):
    
    profile_pic = request.FILES.get('profile_pic')
    user = get_object_or_404(User, pk=user_id)
    user.profile_pic = profile_pic
    user.save()
    return Response('profile_image.views.py')