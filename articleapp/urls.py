#7/29
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = 'articleapp'



urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    #8/2 하고 create.html로
    path('create/', ArticleCreateView.as_view(), name='create'),
    #라우팅하고 detail.html
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    #8/4 라우팅 후 update.html
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    #8/4 라우팅 후 delete.html
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]