from unicodedata import category
from wsgiref import validate
from rest_framework import serializers
from .models import Article, Category
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


class UpdateArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(allow_null=True)

    class Meta:
        model = Article
        fields = ["body", "image1", "image2", "category"]

    def update(self, instance, validated_data):
        if validated_data["category"] is not None:
            print("The category field is not none.")
            cat_name = validated_data["category"]
            if Category.objects.filter(category_name__iexact=cat_name).exists():
                print("This cat is in the database")
                cat_instance = Category.objects.get(category_name__iexact=cat_name)
                print(cat_instance)
                instance.category = cat_instance
            else:
                print("No category with this name please re-check")

        else:
            print("Cat was None")

        if validated_data["image1"] is not None:
            instance.image1 = validated_data["image1"]

        if validated_data["image2"] is not None:
            instance.image2 = validated_data["image2"]

        instance.body = validated_data["body"]
        return instance
