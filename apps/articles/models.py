from django.db import models
from django.urls import reverse
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
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()

    image1 = models.ImageField(upload_to="apps/articles_images/", null=True, blank=True)
    image2 = models.ImageField(upload_to="apps/articles_images/", null=True, blank=True)
    is_published = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article_details", kwargs={"pkid": self.pkid})
