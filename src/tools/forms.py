from django import forms
from .models import SuggestedCommunityTool


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = SuggestedCommunityTool
        fields ='__all__'
        exclude = ('about',)