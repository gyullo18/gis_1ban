#8/5 댓글구현
from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commentapp'

urlpatterns = [
    #8/9 라우팅후 template > commentapp> create
    path('create/', CommentCreateView.as_view(), name='create'),
]