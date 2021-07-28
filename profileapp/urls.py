from django.urls import path
#7/26
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),#어떤 주소로 접근하는지, 로직(as view), name
    #7/28
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update')#라우팅끝, 주소창에 뭘 수정을 받았는지 알아야함-intpk
]
#라우팅 끝 --- profileapp >> 템플릿 디렉토리 생성 >> profile디렉토리 생성 >> html파일