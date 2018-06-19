from django import forms
from .models import Question
from django.contrib.auth.models import User


class QuestionModelForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(QuestionModelForm, self).__init__(*args, **kwargs)
    #     self.fields['respondent'].queryset = User.objects.all()

    class Meta:
        model = Question
        fields = ('title', 'content',)
        widgets = {'content': forms.Textarea(attrs={'class': 'counted'}),
                   }
