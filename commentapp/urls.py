#8/5 댓글구현
from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = 'commentapp'

urlpatterns = [
    #8/9 라우팅후 template > commentapp> create
    path('create/', CommentCreateView.as_view(), name='create'),
    #8/9 deleteview라우팅 후 delete.html
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]