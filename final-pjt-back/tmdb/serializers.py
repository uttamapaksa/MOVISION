from rest_framework import serializers
from .models import Genre, Movie, Actor, MovieComment
from django.contrib.auth import get_user_model

User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')
    like_users = UserSerializer(read_only=True, many=True)
    seen_users = UserSerializer(read_only=True, many=True)
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genres = GenreSerializer(read_only=True, many=True)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    actors = ActorSerializer(read_only=True, many=True)
    
    class MovieCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = MovieComment
            fields = '__all__'
    Movie_comments = MovieCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class MovieSearchSerializer(serializers.ModelSerializer):  #영화 검색용
    similarity = serializers.FloatField(default=0)

    class Meta:
        model = Movie
        fields = ('pk', 'overview', 'title', 'poster_path', 'similarity',)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('Movie',)



# 추천기능
# 사용자가 좋아요 누른 영화 
class UserLikeMovieListSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'words',)

    like_movies = MovieSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies',)

# 여러 영화 제공
class RecommendMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'words', 'poster_path')

# 사용자가 선택 또는 좋아요 한 영화와 비슷한 영화
class UserChoiceSimilarMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'release_date')