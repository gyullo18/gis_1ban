#8/4 createview에 로그인 관련된 보안 끝내고
#인증에 필요한 decorator 함수 작성
#후 update와 deleteview에 작성해준다.
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        #게시글의 작성자와 요청을 보내는 유저가 필요
        target_article = Article.objects.get(pk=kwargs['pk']) #DB에서 가져옴, get에서 단일객체로
        #게시글 안의 writer 인증 과정
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            #권한이 없는 페이지에 접근했다.
            return HttpResponseForbidden()
    return decorated