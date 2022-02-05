
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from .form import ChoiceForm
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

    def get_success_url(self):
        return reverse('poll_check', kwargs={'pk': self.object.poll.pk})


class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = "choice/update.html"
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_check', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = "choice/delete.html"
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_check', kwargs={'pk': self.object.poll.pk})


class AnswerView(TemplateView):
    template_name = 'answer/answer_view.html'
    object = 'answer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context['poll'] = poll
        choice = poll.poll_answer.all('choice')
        context['choice'] = choice
        return context