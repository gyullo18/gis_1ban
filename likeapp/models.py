from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article
# 8/23
# 어떤 게시글에 어떤 유저가 좋아요를 눌렀는지
class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record', null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=False)
    # 한 게시글에는 한 번만 찍을 수 있도록
    class Meta: #필드가 아닌 모든것을 메타데이터로 적용해라.ex)이미지 크기, 사이즈 등 = db조건을 걸 수 있다.
        unique_together = ['user', 'article']