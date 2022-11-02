from django.urls import path
from articles.views import ArticleListView, ArticleDetailView, AddReviewView


urlpatterns = [
        path('', ArticleListView.as_view(), name='article_list'),
        path('<int:id>/', ArticleDetailView.as_view(), name="detail"),
        path('<int:id>/reviews/>', AddReviewView.as_view(), name='reviews')
]