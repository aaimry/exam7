
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from .base import FormView
from .form import ChoiceForm, AnswerForm
from .models import Choice, Poll


class PollView(ListView):
    model = Choice
    context_object_name = "choice"
    template_name = 'choice/choice_index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choice/create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('poll_check', kwargs={'pk': self.object.poll.pk})


class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = "choice/update.html"
    model = Choice
    context_object_name = 'choice'


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = "choice/delete.html"
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_check', kwargs={'pk': self.object.poll.pk})


class AnswerView(FormView):
    template_name = 'answer/answer_view.html'
    object = 'answer'
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context['poll'] = poll
        choice = poll.poll_answer.all()
        context['choice'] = choice
        return context

    def post(self, request, *args, **kwargs):
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = AnswerForm.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll')

    def get_form(self, form_class):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.kwargs.get('pk'), **self.get_form_kwargs())
