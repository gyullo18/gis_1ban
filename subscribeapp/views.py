from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

# 8/19
# 로그인 되어있는 상태여야 함 -- 인증
@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):#get방식을 받았을 때 어떤 작업을 할지
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])#어떤 프로젝트에 요청을 보냈는지

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        #구독정보가 있다면, 구독 취소
        if subscription.exists():
            subscription.delete()
        #없었다면, 새로운 구독 정보를 만들어준다.
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)
    # get요청을 처리하고 나서 어디로 갈지
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':kwargs['project_pk']})
#로직 만들었으니 urls.py에서 라우팅해주어야함


# 8/23 - 구독중인 project의 article만 걸러내는 작업
# 구독을 한사람이기 때문에 로그인 되어있는지 확인 해주자
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=project_list)
        return article_list
#url 라우팅
