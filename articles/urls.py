from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('api/article/', views.ArticleView.as_view(), name="article_view")

]
