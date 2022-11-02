from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse
from .forms import ArticleReviewForm
from .models import Article, Comment


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        article = Article.objects.get(id=id)
        review_form = ArticleReviewForm

        return render(request, 'detail.html', {'article': article, 'review_form': review_form})

class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        article = Article.objects.get(id=id)
        review_form = ArticleReviewForm(data=request.POST)

        if review_form.is_valid():
            Comment.objects.create(
                article=article,
                author=request.user,
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse('detail', kwargs={'id': article.id}))

        return render(request, 'detail.html', {'article': article, 'review_form': review_form})



