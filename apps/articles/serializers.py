from rest_framework import serializers
from .models import Article
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from taggit.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.category_name")
    comments = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "body",
            "image1",
            "image2",
            "category",
            "date_created",
            "date_updated",
            "author",
            "is_published",
            "tags",
            "comments",
        ]

    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_tags(self, obj):
        tags_queryset = obj.tags.all()
        tag_names = []
        for tag in tags_queryset:
            tag_names.append(tag.name)

        return tag_names
