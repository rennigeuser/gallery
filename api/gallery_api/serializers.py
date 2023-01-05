from apps.gallery.models import Image, Like, Post
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url')

    class Meta:
        model = Image
        fields = (
            'image',
        )


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = (
            'author',
            'post',
            'created_at',
            'updated_at',
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    icon = serializers.ReadOnlyField(source='icon.image.url')
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = (
            'author',
            'likes',
            'title',
            'icon',
            'icon_alt',
            'created_at',
            'updated_at',
        )