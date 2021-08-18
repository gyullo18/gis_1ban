from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

#8/18 인증과정 -- 로그인 한 사람만 이용 가능하게
#8/12 forms.py 작성 후 CD/L 시작
#createview
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    # 로직 만들고 url에 라우팅
    #8/18 5분
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object})

# 8/12
#detailview
class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    #url에 라우팅

#8/18
#listview 게시판 목록페이지
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20
    #url에 라우트