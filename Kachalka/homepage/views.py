from django.shortcuts import render
from .models import Statistic
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

def index(request):
    template = 'homepage/index.html'
    statis_list = Statistic.objects.values('date', 'calories', 'time', 'type__name')

    context = {
        'statis': statis_list,
        'best_result': statis_list.values('date', 'calories', 'time'),
        'count': statis_list.aggregate(Count('date')),
        'average_calories': round(statis_list.aggregate(Avg('calories'))['calories__avg']),
        'average_time': average_time(statis_list.values('time')),
    }
    return render(request, template, context)