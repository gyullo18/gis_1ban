
from django.urls import path

from likeapp.views import LikeArticleView
# 8/23
app_name = 'likeapp'

urlpatterns = [
    path('article/<int:article_pk>', LikeArticleView.as_view(), name='article_like')
]