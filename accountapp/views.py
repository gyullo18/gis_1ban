from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
    #7/19#로그인 되었는지 안되었는지 여부 is_auth~
    if request.user.is_authenticated :

        if request.method == 'POST' :

            # 임시데이터 작성
            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp #문제가 생기면 중단점을 잡고 확인을 해야함
            new_hello_world.save()

            hello_world_list = HelloWorld.objects.all()
    #post #redirect #/accounts/hello_world/
            return HttpResponseRedirect(reverse('accountapp:hello_world')) #어떤 앱 안에 있는 헬로 월드로 가라 #reverse로 redirect
    #get
        else :
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'hello_world_list': hello_world_list})
    else :
        return HttpResponseRedirect(reverse('accountapp:login'))
#7/12
#crud start
#create view 상속
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')#클래스에서 리버스를 쓰기위함 why?Class와 Funtion은 불러오는 동선이 달라서 but 어카운트 앱에서 헬로월드로 가는건 같음
    template_name = 'accountapp/create.html'#create.html만드는 건 나중에

#7/15
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'#객체 접근
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    #7/19
    def get(self, request, *args, **kwargs):
        #7/20
        if request.user.is_authenticated and self.get_object() == request.user: #계정객체가 request를 보내는 유저 객체와 동일한지
            return super().get(request, *args, **kwargs) #유저가 들어와 있다면 부모의 메서드를 실행하라

        else :
            #7/20
            return HttpResponseForbidden() #금지된 곳으로 접근했다 = 두번째 객체로 delete/1 페이지들어가면 안들어가짐

    def post(self, request, *args, **kwargs):
        #7/20
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)  # 유저가 들어와 있다면 부모의 메서드를 실행하라

        else:
            #7/20
            return HttpResponseForbidden()


#7/19
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    # 7/19
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)  # 유저가 들어와 있다면 부모의 메서드를 실행하라

        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)  # 유저가 들어와 있다면 부모의 메서드를 실행하라

        else:
            return HttpResponseForbidden()

        #get, post 나중에 바꿀예정