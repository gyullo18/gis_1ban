#7/29
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    #8/2 하고 create.html로
    path('create/', ArticleCreateView.as_view(), name='create'),
]