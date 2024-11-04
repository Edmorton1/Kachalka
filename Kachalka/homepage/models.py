from django.db import models
from datetime import datetime

# Create your models here.


class Types(models.Model):
    name = models.CharField('Тип', max_length=32)

    class Meta:
        verbose_name = 'Тип',
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name

class Statistic(models.Model):
    date = models.DateField('Дата')
    date_str = datetime.strftime(datetime.now(), '%d-%m-%Y')
    calories = models.IntegerField('Калории')
    time = models.TimeField('Время', blank=True, null=True)
    type = models.ForeignKey(
        Types,
        on_delete=models.CASCADE,
        related_name='types',
        verbose_name='Тип',
    )

    class Meta:
        verbose_name = 'Статистика',
        verbose_name_plural = 'Статистика'
    
    def __str__(self):
        return self.date_str

