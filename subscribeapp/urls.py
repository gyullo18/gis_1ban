# 8/19 구독앱 urls
from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    #8/19 구독 정보를 누르는데 어느 게시판에 올릴지
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    #8/23  구독한 정보들을 볼수 있도록
    path('list/', SubscriptionListView.as_view(), name='list'),
]