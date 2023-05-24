from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# from tmdb.models import Movie


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=1)
    nickname = models.TextField(blank=True)
    like_genre = models.IntegerField()
    profile_pic = ProcessedImageField(
        default = '/profileimages/Default-Profile-Image-AA.PNG',
        blank = True,
        null=True,
        upload_to = 'profileimages',
        processors = [ResizeToFill(300, 300)],
        format = 'JPEG',
        options = {'quality':90},
        )