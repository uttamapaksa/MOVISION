from rest_framework import serializers
from .models import Userdata
# from .models import Userdata, LikeMovies, SeenMovies, UserProfile


class UserdataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userdata
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

# class LikeMoviesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = LikeMovies
#         fields = '__all__'
#         # fields = ('id', 'title', 'completed',)

# class SeenMoviesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = SeenMovies
#         fields = '__all__'
#         # fields = ('id', 'title', 'completed',)

# class UserProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = '__all__'
#         # fields = ('id', 'title', 'completed',)