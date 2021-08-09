from django.shortcuts import render

# Create your views here.

from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

#8/9
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    #4분정도
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs = {'pk':self.object.article.pk})
    #url 연결