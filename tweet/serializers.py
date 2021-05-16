from rest_framework import serializers
# from .models import Tweet
from .models import ImageUpload
from django.conf import settings

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'

# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ('email', 'username', 'password')
#         extra_kwargs = {'password': {'write-only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance


# class TweetActionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     action = serializers.CharField()
#     content = serializers.CharField(allow_blank=True, required=False)

#     def validate_action(self, value):
#         value = value.lower().strip()
#         if not value in TWEET_ACTION_OPTIONS:
#             raise serializers.ValidationError('This is not a valid option')
#         return value


# class TweetSerializer(serializers.ModelSerializer):
#     likes = serializers.SerializerMethodField(read_only=True)
#     parent = TweetActionSerializer(read_only=True)
#     # content = serializers.SerializerMethodField(read_only=True)
#     # is_retweet = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Tweet
#         fields = ['id', 'content', 'likes', 'is_retweet']

#     # to use serializer method field we use get_fieldname method
#     def get_likes(self, obj):
#         return obj.likes.count()

#     # to use serializer method field we use get_fieldname method
#     # def get_content(self, obj):
#     #     content = obj.content
#     #     if obj.is_retweet:
#     #         content = obj.parent.content
#     #     return content


# class TweetCreateSerializer(serializers.ModelSerializer):
#     likes = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Tweet
#         fields = ['id', 'content', 'likes']

#     def get_likes(self, value):
#         return obj.likes.count()

#     def validate_content(self, value):
#         if len(value) > MAX_TWEET_LENGTH:
#             raise serializers.ValidationError('This tweet is too long')
#         return value
