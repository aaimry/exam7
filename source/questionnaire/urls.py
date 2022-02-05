from django.urls import path

from .choice import ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView, AnswerView
from .views import PollView, PollCreateView, PollDetailView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('', PollView.as_view(), name='poll'),
    path('add/', PollCreateView.as_view(), name='poll_add'),
    path('check/<int:pk>', PollDetailView.as_view(), name='poll_check'),
    path('check/<int:pk>/update', PollUpdateView.as_view(), name='poll_update'),
    path('check/<int:pk>/delete', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/add/', ChoiceCreateView.as_view(), name='choice_add'),
    path('poll/<int:pk>/update', ChoiceUpdateView.as_view(), name='choice_update'),
    path('poll/<int:pk>/delete', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('poll/<int:pk>/answer/', AnswerView.as_view(), name='answer'),

]
