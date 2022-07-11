from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class AdminArticle(admin.ModelAdmin):
    list_display = ["email", "created"]
