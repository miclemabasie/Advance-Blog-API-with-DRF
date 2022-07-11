from rest_framework import serializers
from .models import Article
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.category_name")
    comments = serializers.SerializerMethodField(read_only=True)

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
            # "tags",
            "comments",
        ]

    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data
