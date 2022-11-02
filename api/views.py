from rest_framework.generics import ListAPIView
from articles.models import Article

from .serializers import LanguageSerializer


class LanguageApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = LanguageSerializer
