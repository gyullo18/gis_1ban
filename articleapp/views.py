from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

#8/2
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article

#createview
#8/4
#로그인이 필요하다라는 인증과정 -- 장고 기본 제공
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    #url 라우팅
    #create.html완성 후
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    #8/4 -- success_url helloworld를 없애고 detail페이지로 돌아갈 수 있도록
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

#8/2 readview
#아무나 들어갈 수 있어야함. -- 인증과정 x
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    #url 라우팅

#8/4 updateview
#게시글 작성자만 수정하거나 삭제할 수 있게
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})
    #urls 들어가서 라우팅

#8/4 deleteview
#게시글 작성자만 수정하거나 삭제할 수 있게
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'
    #url 라우팅



