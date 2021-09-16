from datetime import timedelta,datetime
todayDatetime = datetime.now() + timedelta(hours=9)
print("%04d-%02d-%02d"%(todayDatetime.year,todayDatetime.month,todayDatetime.day))