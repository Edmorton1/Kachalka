from django.contrib import admin

# Register your models here.
from .models import Statistic, Types

class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'calories',
        'time',
        'type',
    )
    list_editable = (
        'date',
        'calories',
        'time',
        'type',
    )

admin.site.register(Statistic)
admin.site.register(Types)
