from django.db import models

# Create your models here.


class Types(models.Model):
    name = models.CharField('Тип', max_length=32)

class Statistic(models.Model):
    date = models.DateField('Дата')
    calories = models.IntegerField('Калории')
    time = models.TimeField('Время')
    type = models.ForeignKey(
        Types,
        on_delete=models.CASCADE,
        related_name='types',
    )
