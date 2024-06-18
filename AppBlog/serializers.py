from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Comment,Category,Blog
from django.contrib.auth.models import User
class BlogSerializer(ModelSerializer):
    author_name=serializers.ReadOnlyField(source="author.username")
    category_name=serializers.ReadOnlyField(source="category.name")
    class Meta:
        model=Blog
        fields=[
            "title",
            "content",
            'category_name',
            'author_name',
            'create',
            'slug',
        ]

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=["name",'create']
class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=["name","Email","content","post","create","active"]

