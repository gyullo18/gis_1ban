#7/26
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    #뭘 만들건지
    model = Profile #프로필 앱안의 모델
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')#다 만들고 어디로 돌아갈지 #콜론 앞의 accountapp - app_name이 들어감
    template_name = 'profileapp/create.html'#프로필 생성페이지를 어떤html로 사용할지

    #라우팅 --- profileapp > urls
#7/26
    #부모에 있는 form_valid 호출
    def form_valid(self, form):
        form.instance.user = self.request.user #정상적인 유저 객체를 받아야함
        return super().form_valid(form)

#7/28
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    #url 라우팅연결