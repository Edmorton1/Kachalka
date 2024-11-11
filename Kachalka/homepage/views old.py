from django.shortcuts import render
from .models import Statistic, Records
from django.db.models import Avg, Count
import datetime


# Create your views here.

def average_time(a):
    hours = 0
    minutes = 0
    for i in range(len(a)):
        hours += a[i]['time'].hour
        minutes += a[i]['time'].minute
    return (int(hours / len(a) * 60 + minutes / len(a))//60, int(hours / len(a) * 60 + minutes / len(a)) % 60)

def day_after(dat):
    return ((datetime.datetime.now().date() - dat).days)

def best_result(a):
    maximum = 0
    date = 0
    calories = 0
    for i in a:
        date = i['date']
        time = i['time']
        calories = i['calories']
        maximum = max(maximum, calories)
    for i in a:
        if i['calories'] == maximum:
            date = i['date']
            time = i['time']
            days = day_after(date)
            return (date, maximum, time, days)

def index(request):
    template = 'homepage/index.html'
    statis_list = Statistic.objects.values('date', 'calories', 'time', 'type__name')
    records = Records.objects.values('exercise', 'record', 'date')

    records_with_days = []
    for record in records:
        days_since_record = day_after(record['date'])
        records_with_days.append({
            'exercise': record['exercise'],
            'record': record['record'],
            'date': record['date'],
            'days_since_record': days_since_record
        })

    context = {
        'statis': statis_list,
        'best_result': best_result(statis_list.values('date', 'calories', 'time')),
        'count': statis_list.aggregate(Count('date')),
        'average_calories': round(statis_list.aggregate(Avg('calories'))['calories__avg']),
        'average_time': average_time(statis_list.values('time')),

        'records': records_with_days,
    }
    return render(request, template, context)