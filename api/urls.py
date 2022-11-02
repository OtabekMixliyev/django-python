from django.urls import path
from .views import LanguageApiView

urlpatterns = [
    path('', LanguageApiView.as_view())
]