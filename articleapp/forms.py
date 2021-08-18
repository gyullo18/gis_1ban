#8/2
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        # 8/18 project추가 -- 어떤 게시판으로 이동할지
        #view로