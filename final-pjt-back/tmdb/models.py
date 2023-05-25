
from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)   #장르명

class Actor(models.Model):
    name = models.CharField(max_length=50)    #배우명
    poster_path = models.CharField(max_length=200, blank=True, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100) #제목
    release_date = models.DateField(blank=True)  # 개봉일
    popularity = models.FloatField()  #인기
    vote_count = models.IntegerField()  #평점수
    vote_average = models.FloatField()  #평점
    overview = models.TextField()   #개요
    poster_path = models.CharField(max_length=200, blank=True)   #이미지
    backdrop_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)   #유튜브
    genres = models.ManyToManyField(Genre, blank=True)   #장르
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True) # 좋아요 누른 사람
    seen_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="seen_movies", blank=True) # 봤어요 누른
    actors = models.ManyToManyField(Actor, blank=True)  #배우

    words = models.TextField(null=True)  #추천기능용

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name="user_movie_comments")
    movie = models.ForeignKey(Movie, related_name="movie_comments", on_delete=models.CASCADE)
    content =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)