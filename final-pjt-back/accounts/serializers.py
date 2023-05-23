from allauth.account.adapter import get_adapter
from .models import User
from tmdb.models import Movie
from articles.models import Review, Review_Comment
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


# 회원가입 시에 쓸 dj-rest-auth 커스텀 등록
class CustomRegisterSerializer(RegisterSerializer):
    level = serializers.IntegerField(default=1)
    exp = serializers.IntegerField(default=1)
    nickname = serializers.CharField()
    like_genre = serializers.ChoiceField(choices=User.GENRECHOICE)


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'level', 'exp', 'nickname')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'level': self.validated_data.get('level', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'exp': self.validated_data.get('exp', ''),
            'like_genre': self.validated_data.get('like_genre', ''),
            # 'created_at': self.validated_data.get('created_at', ''),
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.level = self.cleaned_data.get('level')
        user.nickname = self.cleaned_data.get('nickname')
        user.exp = self.cleaned_data.get('exp')
        user.like_genre = self.cleaned_data.get('like_genre')
        # user.created_at = self.cleaned_data.get('created_at')
        user.save()
        adapter.save_user(request, user, self)
        return user


# 유저 데이터를 가져올 때 쓸 모든 필드, 참조, 역참조 값
class UserSerializer(serializers.ModelSerializer):

    # Review 모델에서 필요한 필드와 역참조값 불러오기
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title', 'created_at',)
    reviews = ReviewSerializer(many=True, read_only=True)


    # Review_Comment 모델에서 필요한 필드와 역참조값 불러오기
    class ReviewCommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review_Comment
            fields = '__all__'
    reviewcomments = ReviewCommentSerializer(many=True, read_only=True)

    # Movie 모델에서 필요한 필드와 역참조값 불러오기
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'vote_average',)
    like_movies = MovieSerializer(many=True)
    seen_movies = MovieSerializer(many=True)
    
    # User 모델에서 필요한 필드와 참조값 불러오기
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'nickname')
    followings = FollowingSerializer(many=True, read_only=True)
    
    # User 모델에서 필요한 필드와 역참조값 불러오기
    class FollowerSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'nickname')
    followers = FollowerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'