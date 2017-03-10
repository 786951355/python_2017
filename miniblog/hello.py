from datetime import datetime, timedelta

delta = timedelta(minutes=30)

start =  datetime(2017, 3, 8, 12, 6, 35, 544302)
now = datetime.now()
m = now - start

print(now)
print(start)
print(m.total_seconds())
