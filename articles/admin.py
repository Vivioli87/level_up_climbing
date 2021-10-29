from django.contrib import admin
from .models import Article, ArticleComments

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    fields = ('title', 'content', 'image_url', 'image')


class ArticleCommentsAdmin(admin.ModelAdmin):

    fields = ('article', 'user_profile', 'title', 'comment')


admin.site.register(ArticleComments, ArticleCommentsAdmin)
