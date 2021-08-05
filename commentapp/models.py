from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

#8/5 댓글 구현 모델
class Comment(models.Model):
    #어떤 게시글과 연결 되어 있는지 , 해당 게시글이 삭제될 때 어쩔 것인지
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #form.py 생성