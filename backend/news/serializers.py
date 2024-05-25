from rest_framework import serializers
from .models import New, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields = ['id', 'title', 'description', 'image', 'tags', 'likes', 'dislikes', 'views']
