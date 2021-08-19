from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 8/19
#어떤 유저가 어떤 게시판을 구독했는가
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    #구독 정보가 여러개 생기지 않게 -- 쌍이 존재한다면 저장이 두개 이상 생기지 않음
    class Meta: #외부 설정 -- field가 아닌 외부적인 조건들
        unique_together = ['user', 'project']