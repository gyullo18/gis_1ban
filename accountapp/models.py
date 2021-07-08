from django.db import models

# Create your models here.

class HelloWorld(models.Model): #기본적인 장고 모델 완성
    text = models.CharField(max_length=255, null=False) #텍스트라는 속성에 모델스 안의 캐릭터필드에 최대값 255와 공백이 없어야 한다.
#연결고리 만들기 makemigrations --- terminal
#어카운트 앱에서 변화가 생겼다 --- 헬로월드라는 모델이 새로 생겼다 --