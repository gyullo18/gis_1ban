#8/2
from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # 8/26 컨텐트 커스터마이징 -- WYSIWYG를 하는데 있어서 .editable를 위한 부분
    # WYS
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align: left;'
                                                                    'min-height: 10rem;'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        # 8/18 project추가 -- 어떤 게시판으로 이동할지
        #view로