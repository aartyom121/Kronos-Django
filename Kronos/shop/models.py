from django.db import models


class Category(models.Model):
    cat = models.CharField('Категория', max_length= 30)
    def __str__(self):
        return self.cat

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='images/shop', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shop/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# 'media/images/shop/img/%Y/%m/%d'