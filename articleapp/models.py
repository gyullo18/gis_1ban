from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#8/2
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)#1대 다 연결, 유저가 접근하는 이름
    # 8/18 projectapp과 연결 -- 게시판과 게시글의 연결
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)#미디어라는 폴더 안에 article이라는 폴더가 생겨서 사진저장
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)#언제 작성했는지에 대한 정보
    #모델 완성 - migration
#forms.py 만들기

