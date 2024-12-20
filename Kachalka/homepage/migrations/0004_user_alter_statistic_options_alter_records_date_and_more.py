# Generated by Django 5.1.2 on 2024-11-14 15:00

import datetime
import django.utils.timezone
import homepage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_records_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Имя')),
                ('link', models.CharField(max_length=512, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Пользовательская ссылка',
                'verbose_name_plural': 'Пользовательские ссылки',
            },
        ),
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ('-id', 'date'), 'verbose_name': 'Статистика', 'verbose_name_plural': 'Статистика'},
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[homepage.validators.max_date], verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='records',
            name='record',
            field=models.IntegerField(validators=[homepage.validators.min_cal], verbose_name='Рекорд'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='calories',
            field=models.IntegerField(validators=[homepage.validators.min_cal], verbose_name='Калории'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[homepage.validators.max_date], verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='time',
            field=models.TimeField(default=datetime.time(0, 0), validators=[homepage.validators.min_time], verbose_name='Время'),
        ),
    ]
