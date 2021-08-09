#8/9 메서드 데코레이터 작성
from django.http import HttpResponseForbidden

from commentapp.models import Comment

#13분 30초 정도
def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
        return decorated