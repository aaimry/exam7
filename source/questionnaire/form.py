from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from .models import Poll, Choice, Answer


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


class AnswerForm(forms.ModelForm):
    choice = forms.ModelChoiceField(queryset=None, widget=widgets.RadioSelect)

    def __init__(self, pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(poll__pk=pk)

    class Meta:
        model = Answer
        fields = ["choice"]
