from django.db import models
from apps.commons.models import TimeStampUUIDModel
from apps.profiles.models import Profile
from taggit.managers import TaggableManager
from taggit.models import Tag


class Category(TimeStampUUIDModel):
    category_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Article(TimeStampUUIDModel):
    author = models.ForeignKey(
        Profile, related_name="articles", on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()

    image1 = models.ImageField(upload_to="articles/", null=True, blank=True)
    image2 = models.ImageField(upload_to="articles/", null=True, blank=True)
    is_published = models.BooleanField(default=True)
    tags = TaggableManager()
