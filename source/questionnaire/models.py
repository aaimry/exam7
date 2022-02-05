from django.db import models
from django.urls import reverse


class Poll(models.Model):
    question = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Вопрос')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def get_absolute_url(self):
        return reverse('poll_check', kwargs={'pk': self.pk})

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'Poll'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    choice_text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Вариант')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='poll',
                             verbose_name='Опрос')

    def get_absolute_url(self):
        return reverse('poll_check', kwargs={'pk': self.poll.pk})

    def __str__(self):
        return f'{self.choice_text} : {self.poll}'

    class Meta:
        db_table = 'Choice'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='poll_answer',
                             verbose_name='Опрос')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата заполнения')
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='choice_answer', verbose_name='Вариант')

    def __str__(self):
        return f'{self.poll} : {self.choice}'

    class Meta:
        db_table = 'Answer'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
