from django.contrib import admin

from .models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'create_date']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['question']


admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'poll']
    list_filter = ['choice_text']
    search_fields = ['choice_text']
    fields = ['choice_text', 'poll']


admin.site.register(Choice, ChoiceAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['poll', 'choice', 'datetime']
    list_filter = ['poll']
    search_fields = ['poll']
    fields = ['poll', 'choice']

    
admin.site.register(Answer, AnswerAdmin)