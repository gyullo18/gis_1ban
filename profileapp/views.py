#7/26
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

#7/28
#보안처리
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    #뭘 만들건지
    model = Profile #프로필 앱안의 모델
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'#프로필 생성페이지를 어떤html로 사용할지

    #라우팅 --- profileapp > urls
#7/26
    #부모에 있는 form_valid 호출
    def form_valid(self, form):
        form.instance.user = self.request.user #정상적인 유저 객체를 받아야함
        return super().form_valid(form)
    #7/28
    # 다 만들고 어디로 돌아갈지
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})


#7/28
#login_required가 필요 없기 때문에 리스트로 하지않음
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    #url 라우팅연결

    #메서드를 통해 동적으로 success url을 받아줌 -- 원하고자 하는 페이지를 넣을 수 있음
    #다른 곳에도 적용
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})#추가인자 넣어주기

