#8/12
from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

urlpatterns = [
    #8/12 라우팅 후 create.html만들기
    path('create/', ProjectCreateView.as_view(), name='create'),
    #8/12 라우팅 후 detail.html만들기
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
]