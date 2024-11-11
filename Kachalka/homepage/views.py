from django.shortcuts import render
from .models import Statistic, Records
from .forms import RecordsForm
from django.db.models import Avg, Count
import datetime

# Вспомогательные функции

def average_time(a):
    hours = 0
    minutes = 0
    for i in range(len(a)):
        hours += a[i]['time'].hour
        minutes += a[i]['time'].minute
    return (int(hours / len(a) * 60 + minutes / len(a))//60, int(hours / len(a) * 60 + minutes / len(a)) % 60)

def day_after(dat):
    return (datetime.datetime.now().date() - dat).days

def best_result(a):
    maximum = 0
    date = None
    time = None
    calories = 0
    for i in a:
        if i['calories'] > maximum:
            maximum = i['calories']
            date = i['date']
            time = i['time']
    days = day_after(date) if date else None
    return date, maximum, time, days

# Представления

def statis():
    """Возвращает статистические данные для главной страницы."""
    statis_list = Statistic.objects.values('date', 'calories', 'time', 'type__name')
    best = best_result(statis_list)
    count = statis_list.aggregate(Count('date'))
    average_calories = round(statis_list.aggregate(Avg('calories'))['calories__avg'])
    avg_time = average_time(statis_list.values('time'))

    return {
        'statis': statis_list,
        'best_result': best,
        'count': count,
        'average_calories': average_calories,
        'average_time': avg_time,
    }

def records():
    """Возвращает данные о рекордах, включая дни с момента установления рекорда."""
    records = Records.objects.values('exercise', 'record', 'date')
    records_with_days = [
        {
            'exercise': record['exercise'],
            'record': record['record'],
            'date': record['date'],
            'days_since_record': day_after(record['date']),
        }
        for record in records
    ]
    return {'records': records_with_days}

def index(request):
    """Главное представление, объединяющее данные статистики и рекордов."""
    template = 'homepage/index.html'
    context = {**statis(), **records()}
    return render(request, template, context)

def radd(request):
    form = RecordsForm(request.POST or None)
    template = 'homepage/index.html'
    if form.is_valid():
        form.save()
    context = {'form': form,
               **statis(), **records()}
    return render(request, template, context)