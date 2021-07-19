#7/19
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    #오버라이빙
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)#이니셜라이즈 할때 선택적 매개변수를 다 받을 것이며, 부모의 모든 변수에 다 넣어주겠다.

        self.fields['username'].disabled = True

