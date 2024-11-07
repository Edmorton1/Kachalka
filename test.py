import datetime

a = [{'date': datetime.date(2024, 9, 3), 'calories': 239, 'time': datetime.time(0, 35)}, {'date': datetime.date(2024, 9, 1), 'calories': 110, 'time': datetime.time(1, 20)}, {'date': datetime.date(2024, 8, 28), 'calories': 431, 'time': datetime.time(0, 55)}, {'date': datetime.date(2024, 8, 26), 'calories': 210, 'time': datetime.time(0, 29)}, {'date': datetime.date(2024, 8, 25), 'calories': 202, 'time': datetime.time(0, 36)}]
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
            return (date, maximum, time)


#             timedelta = datetime.timedelta(hours=time.hour, minutes=time.minute)