from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # through : id 말고 다른 데이터도 넣고 싶을 땐 through 를 통해 중개 테이블을 수동으로 설정할 수 있음
    like_movies = models.ManyToManyField(Movie, related_name='like_users', through='MovieLike')
    seen_movies = models.ManyToManyField(Movie, related_name='seen_users', through='MovieSeen')
    email = models.EmailField(max_length=200)
    nickname = models.CharField(max_length=20, blank=True) 
    profile_image = models.ImageField(blank=True, null=True)
    # 문자열 기반 필드는 null True 금지!
