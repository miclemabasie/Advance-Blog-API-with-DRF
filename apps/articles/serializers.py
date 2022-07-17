from unicodedata import category
from wsgiref import validate
from rest_framework import serializers
from .models import Article, Category
from apps.profiles.models import Profile
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from taggit.models import Tag
from .validators import validate_category, validate_body


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.category_name")
    comments = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="articles:article_details", lookup_field="pkid"
    )

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
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
            "url",
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

    def get_details(self, obj):
        return obj.get_absolute_url()


class UpdateArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(allow_null=True)

    class Meta:
        model = Article
        fields = ["title", "body", "image1", "image2", "category"]

    def validate_title(self, value):
        titles = []
        if Article.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError("A post with this titlie already exists.")
        return value

    def validate_category(self, value):
        if value is not None:
            cats = Category.objects.all()

            cat_names = []
            for cat in cats:
                cat_names.append(cat.category_name)

            if value not in cat_names:
                raise serializers.ValidationError(
                    "This Category doesn't exist at the moment."
                )

            return value
        return None

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


class CreateArticleSerializer(serializers.ModelSerializer):

    tags = serializers.CharField()
    category = serializers.CharField(validators=[validate_category])

    class Meta:
        model = Article
        fields = [
            "title",
            "body",
            "category",
            "image1",
            "image2",
            "is_published",
            "tags",
        ]

    def validate_body(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError("The body of the post can not be empty.")

    def validate_title(self, value):
        if Article.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError(
                "An article with this title already exist in the database."
            )
        else:
            return value

    def create(self, validated_data):
        tags = validated_data["tags"]
        print(tags)
        tag_list = tags.split(",")
        user = self.context["request"].user
        profile = Profile.objects.get(user=user)
        title = validated_data["title"]
        image1 = validated_data["image1"]
        image2 = validated_data["image2"]
        is_published = validated_data["is_published"]
        category = validated_data["category"]
        category = Category.objects.get(category_name__iexact=category)
        article = Article.objects.create(
            author=profile,
            title=title,
            image1=image1,
            image2=image2,
            is_published=is_published,
            category=category,
        )
        print("###############################################")

        for tag in tag_list:
            print(tag)
            article.tags.add(tag)
        article.save()

        return article
