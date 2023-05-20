from rest_framework import serializers
from .models import Genre, Movie, Actor


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)