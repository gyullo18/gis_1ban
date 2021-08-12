from django.forms import ModelForm

from projectapp.models import Project

# 8/12
class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description']
