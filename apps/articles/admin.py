from django.contrib import admin
from .models import Article
from .models import Category


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ["pkid", "id", "author", "is_published"]


admin.site.register(Category)
