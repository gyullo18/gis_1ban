from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_reqired
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#7/20 decorator
@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    #7/19#로그인 되었는지 안되었는지 여부 is_auth~
    #7/20if else지우기
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

#7/12
#crud start
#create view 상속
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/create.html'#create.html만드는 건 나중에

    #7/28
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

#7/15
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'#객체 접근
    template_name = 'accountapp/detail.html'

#7/20 메서드에 적용하기 위한 decorator
#메서드 데이터의 장점 - 리스트로 인자를 받을 수 있음
has_ownership = [login_required, account_ownership_reqired]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    # 7/28
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

    #7/20 get에 @login_required를 쓰면 메서드기 때문에 적용 안됨

#7/20
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

