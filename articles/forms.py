from django import forms

from articles.models import Comment


class ArticleReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)