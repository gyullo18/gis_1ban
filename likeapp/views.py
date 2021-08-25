from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import RedirectView


from articleapp.models import Article
from likeapp.models import LikeRecord

# 8/23 댓글에도 적용 가능
# 로그인 되어있어야 로직 실행
@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        #어떤 유저가 좋아요를 누르려고 요청을 보냈는지
        user = request.user
        #어떤 게시글에 좋아요를 눌렀는지 -게시글 확보
        article = Article.objects.get(pk=kwargs['article_pk'])

        #위 두개의 조건을 만족하는 여부 -- 좋아요 기록을 찾자
        likeRecord = LikeRecord.objects.filter(user=user,
                                               article=article)

        #만약에 없다면 좋아요 찍어주기
        if likeRecord.exists(): #존재한다면 detail 페이지로 다시 돌아감
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']}))
        else: #아니라면 좋아요 추가 및 저장
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
    #url 라우팅