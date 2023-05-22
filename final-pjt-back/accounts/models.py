from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# from tmdb.models import Movie


# Create your models here.
class User(AbstractUser):
    pass
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # # through : id 말고 다른 데이터도 넣고 싶을 땐 through 를 통해 중개 테이블을 수동으로 설정할 수 있음
    # like_movies = models.ManyToManyField(Movie, related_name='like_users', through='MovieLike')
    # seen_movies = models.ManyToManyField(Movie, related_name='seen_users', through='MovieSeen')
    # email = models.EmailField(max_length=200)
    # nickname = models.CharField(max_length=20, blank=True) 
    # # 문자열 기반 필드는 null True 금지!

class Userdata(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=1)
    nickname = models.TextField(blank=True)
    # favorite_genres = models.IntegerField()
    # profile_image = models.ImageField()
    
    
# class LikeMovies(models.Model):
#     user = models.ForeignKey(Userdata, on_delete=models.CASCADE)
#     user = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
# class SeenMovies(models.Model):
#     user = models.ForeignKey(Userdata, on_delete=models.CASCADE)
#     user = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
# class UserProfile(models.Model):
#     user = models.ForeignKey(Userdata, on_delete=models.CASCADE)
#     profile_image = models.ImageField(blank=True, null=True)