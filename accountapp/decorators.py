#7/20 데코레이터도 함수...
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_reqired(func): #account의 소유권이 필요하다. -- 함수를 받음
    def decorated(request, *args, **kwargs): #감싸질 새로운 함수
        target_user = User.objects.get(pk=kwargs['pk']) #이 페이지 주인- 데이터 베이스에서 접근 = 유저라는 특정 object +primary key=원하는 객체 + user라는 객체
        if target_user == request.user:
            return func(request, *args, **kwargs) #받은 함수를 그대로 실행
        else:
            return HttpResponseForbidden() #금지된 곳에 접근했다
    return decorated #완성되었으니 decorated라는 내부함수를 다시 반환해준다