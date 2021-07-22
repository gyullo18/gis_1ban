from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta: #실질적인 정보를 제외한 나머지 정보-- 설명해주는 정보 = 메타정보
        model = Profile
        fields = ['image', 'nickname', 'message']#입력받을 필드들이 뭔지
