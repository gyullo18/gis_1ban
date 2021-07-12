from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST' :

        # 임시데이터 작성
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
#post #redirect #/accounts/hello_world/
        return HttpResponseRedirect(reverse('accountapp:hello_world')) #어떤 앱 안에 있는 헬로 월드로 가라 #reverse로 redirect
#get
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})


