from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_reqired
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#7/20 decorator
from articleapp.models import Article

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
#8/19 project detailview와 같이 만들어줌
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'#객체 접근
    template_name = 'accountapp/detail.html'

    # 8/19
    paginate_by = 20
    # 8/19
    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)

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
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'

