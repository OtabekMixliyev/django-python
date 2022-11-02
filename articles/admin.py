from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)

class ArticleAdminReview(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, ArticleAdminReview)
