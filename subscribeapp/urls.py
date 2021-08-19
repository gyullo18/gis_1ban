# 8/19 구독앱 urls
from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    #8/19 구독 정보를 누르는데 어느 게시판에 올릴지
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe')
]