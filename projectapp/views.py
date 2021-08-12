from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


#8/12 forms.py 작성 후 CD/L 시작
#createview
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'
    # 로직 만들고 url에 라우팅