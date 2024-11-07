from django.contrib import admin

# Register your models here.
from .models import Statistic, Types, Records

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

class RecordsAdmin(admin.ModelAdmin):
    list_display = (
        'exercise',
        'record',
    )
    list_editable = (
        'exercise',
        'record',
    )

admin.site.register(Records)
admin.site.register(Statistic)
admin.site.register(Types)
