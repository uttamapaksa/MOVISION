
from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)   #장르명

class Actor(models.Model):
    name = models.CharField(max_length=50)    #배우명

class Movie(models.Model):
    title = models.CharField(max_length=100) #제목
    release_date = models.DateField(blank=True)  # 개봉일
    popularity = models.FloatField()  #인기
    vote_count = models.IntegerField()  #평점수
    vote_average = models.FloatField()  #평점
    overview = models.TextField()   #개요
    poster_path = models.CharField(max_length=200)   #이미지
    youtube_key = models.CharField(max_length=100)   #유튜브
    genres = models.ManyToManyField(Genre, blank=True)   #장르
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True) #좋아요한사람수
    actors = models.ManyToManyField(Actor, blank=True)  #배우


class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="TMDB_Comment", on_delete=models.DO_NOTHING)
    content =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)