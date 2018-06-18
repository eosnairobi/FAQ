from django import forms
from .models import Question


class QuestionModelForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'content', 'respondent')
        widgets = {'next_visit': forms.DateInput(attrs={'class': 'form-control dateinput'}),
                   'respondent': forms.Select(attrs={'class': 'selectpicker',
                                                     'data-live-search': 'true',
                                                     'title': 'Select St'}),
                   }
