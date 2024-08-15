from django.db import models
from django.utils.timezone import now
from users.models import User
import datetime


class Test(models.Model):
    name = models.CharField('Название теста', max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    question = models.CharField('Вопрос', max_length=200)
    cor_ans = models.CharField('Корректный ответ', max_length=200)
    uncor_ans1 = models.CharField('Некорректный ответ 1', max_length=200)
    uncor_ans2 = models.CharField('Некорректный ответ 2', max_length=200)
    uncor_ans3 = models.CharField('Некорректный ответ 3', max_length=200)
    test_number = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return f'/tests/{self.id}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    test_name = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)
    ans1 = models.CharField('Выбранный ответ 1', max_length=300)
    ans2 = models.CharField('Выбранный ответ 2', max_length=300)
    ans3 = models.CharField('Выбранный ответ 3', max_length=300)
    ans4 = models.CharField('Выбранный ответ 4', max_length=300)
    ans5 = models.CharField('Выбранный ответ 5', max_length=300)
    ans6 = models.CharField('Выбранный ответ 6', max_length=300)
    ans7 = models.CharField('Выбранный ответ 7', max_length=300)
    ans8 = models.CharField('Выбранный ответ 8', max_length=300)
    ans9 = models.CharField('Выбранный ответ 9', max_length=300)
    ans10 = models.CharField('Выбранный ответ 10', max_length=300)
    res1 = models.CharField('Результат 1', max_length=300, default=0)
    res2 = models.CharField('Результат 2', max_length=300, default=0)
    res3 = models.CharField('Результат 3', max_length=300, default=0)
    res4 = models.CharField('Результат 4', max_length=300, default=0)
    res5 = models.CharField('Результат 5', max_length=300, default=0)
    res6 = models.CharField('Результат 6', max_length=300, default=0)
    res7 = models.CharField('Результат 7', max_length=300, default=0)
    res8 = models.CharField('Результат 8', max_length=300, default=0)
    res9 = models.CharField('Результат 9', max_length=300, default=0)
    res10 = models.CharField('Результат 10', max_length=300, default=0)
    date = models.DateTimeField('Дата прохождения', default=None)

    def __str__(self):
        return f"{self.user.username} - {self.test_name.name}"

    def get_absolute_url(self):
        return f'/tests/{self.id}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = now()  # установить текущую дату и время
        super().save(*args, **kwargs)