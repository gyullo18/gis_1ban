from django.db import models

# Create your models here.
# 8/12
class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

# migration, mitrate
#forms.py만들기

    # 8/18
    # 이 프로젝트의 이름을 str을 이용해 그대로 출력해주겠다. -- 몇번 게시판 객체가 아닌 게시판 이름이 선택됨.
    def __str__(self):
        return f'{self.name}'