from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('Login/', LoginView.as_view(template_name='accountapp/Login.html'),
         name='login'),

    path('Logout/', LogoutView.as_view(template_name='accountapp/Logout.html'),
         name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),#클래스를 함수로 뱉어주는 메서드 #라우트

    #7/15
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]

#app >name으로