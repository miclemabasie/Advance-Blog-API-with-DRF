from django.db import models
from django.conf import settings
from apps.commons.models import TimeStampUUIDModel
from apps.articles.models import Article

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
