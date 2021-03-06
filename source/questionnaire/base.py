from django.shortcuts import render, redirect
from django.views import View

from questionnaire.form import AnswerForm
from questionnaire.models import Answer


class FormView(View):
    form_class = None
    template_name = None
    redirect_url = ''

    def get_redirect_url(self):
        return redirect(self.redirect_url)

    def get(self, request, *args, **kwargs):
        form = self.form_class(pk=self.kwargs.get('pk'))
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid
        return self.form_invalid

    def form_valid(self, form):
        return self.get_redirect_url()

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context)

    def get_context_data(self, **kwargs):
        return kwargs
