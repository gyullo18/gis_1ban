from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

#8/18 인증과정 -- 로그인 한 사람만 이용 가능하게
#8/12 forms.py 작성 후 CD/L 시작
#createview
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    # 로직 만들고 url에 라우팅
    #8/18 5분
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

# 8/12
# 8/18 MultipleObjectMixin으로 detailview에 listview를 덧붙여주자
#detailview
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    #url에 라우팅

    # 8/18
    paginate_by = 20
    # 8/18
    def get_context_data(self, **kwargs):
        # 8/23 구독 여부 확인
        user = self.request.user
        project = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)
        else:
            subscription = None

        # 어떤 게시글들을 넣어줄 것인가, 조건을 걸러내는 메서드 -- 그 게시판 내의 리스트들만 담아준다.
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,#8/19
                                        **kwargs)

#8/18
#listview 게시판 목록페이지
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20
    #url에 라우트