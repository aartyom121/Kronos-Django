from django.db import models


class Players(models.Model):
    amplua_choices = (
        ('', 'Выберите амплуа'),
        ('Доигровщик', 'Доигровщик'),
        ('Центральный блокирующий', 'Центральный блокирующий'),
        ('Связующий', 'Связующий'),
        ('Диагональный', 'Диагональный'),
        ('Либеро', 'Либеро'),
    )
    name = models.CharField('Имя',max_length=15)
    surname = models.CharField('Фамилия', max_length=15)
    gaming_number = models.IntegerField('Игровой номер')
    amplua = models.CharField('Амплуа', max_length=40, choices=amplua_choices)

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return f'/players/{self.id}'

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'