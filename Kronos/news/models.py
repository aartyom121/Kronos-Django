from django.db import models
from django.utils.timezone import now

from users.models import User


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = now()  # установить текущую дату и время
        super().save(*args, **kwargs)