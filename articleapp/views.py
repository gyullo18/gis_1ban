from django.shortcuts import render

# Create your views here.

#8/2
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'articleapp/create.html'

    #url 라우팅
    #create.html완성 후
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)