from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="comment.email", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "email",
            "content",
            "created",
        ]
