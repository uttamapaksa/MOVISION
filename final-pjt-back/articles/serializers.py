from rest_framework import serializers
from .models import Review, Review_Comment ,Party ,Party_Comment


class ReviewListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')


class Review_CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review_Comment
        fields = '__all__'
        # read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    review_comment_set = Review_CommentSerializer(many=True, read_only=True)
    review_comment_count = serializers.IntegerField(source='review_comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('user', )



class PartyListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Party
        fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')


class Party_CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Party_Comment
        fields = '__all__'
        # read_only_fields = ('party',)


class PartySerializer(serializers.ModelSerializer):
    Party_comment_set = Party_CommentSerializer(many=True, read_only=True)
    Party_comment_count = serializers.IntegerField(source='Party_comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Party
        fields = '__all__'
        # read_only_fields = ('user', )



