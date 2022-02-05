from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .form import PollForm, SearchForm
from .models import Poll


class PollView(ListView):
    model = Poll
    context_object_name = "polls"
    template_name = "poll/poll_index.html"
    paginate_by = 4
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            print(self.search_value)
            query = Q(question__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by("-create_date")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class PollDetailView(DetailView):
    template_name = 'poll/check.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        check_poll = get_object_or_404(Poll, pk=kwargs.get('object').id)
        context['check_poll'] = check_poll
        return context


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/create.html'

    def get_success_url(self):
        return reverse('poll_check', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = "poll/update.html"
    model = Poll
    context_object_name = 'poll'


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "poll/delete.html"
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll')