from django import forms
from django.core.exceptions import ValidationError

from .models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['create_date']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
