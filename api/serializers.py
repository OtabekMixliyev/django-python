from rest_framework import serializers
from articles.models import Article


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'summary', 'author', 'date')
