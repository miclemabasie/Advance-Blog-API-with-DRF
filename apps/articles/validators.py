from rest_framework import validators, serializers
from apps.articles.models import Article, Category


def validate_category(value):
    if value is not None:
        cats = Category.objects.all()
        # for cat in cats:
        #     cat_names.append(cat.category_name)
        if cats.filter(category_name__iexact=value).exists():
            return value
        else:
            raise serializers.ValidationError(
                f"The Category {value} doesn't exist at the moment."
            )

    return None


def validate_body(value):
    if len(value) <= 0:
        raise serializers.ValidationError("The body of the post can not be empty.")
