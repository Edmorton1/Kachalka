import datetime

f = datetime.datetime.now().date()
s = datetime.date(year= 2028, month=12, day= 8)
print((s - f).days)