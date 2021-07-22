from django.contrib.auth.models import User
from django.db import models

#7/22
class Profile(models.Model): #profile 모델 생성
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile') #유저와 프로필 1대1 연결, on_delete -user라는 객체가 사라지면 프로필도 지워주겠다 VS SET_NULL
    image = models.ImageField(upload_to='profile/', null=True) #upload_to 어디로 업로드 할것이냐 -- 경로, 이미지 안올리더라도 허용
    nickname = models.CharField(max_length=30, unique=True) #닉네임은 문자열이기때문에 캐릭터필드, 중복안됨
    message = models.CharField(max_length=200, null=True) #대화명 안적어도 허용
