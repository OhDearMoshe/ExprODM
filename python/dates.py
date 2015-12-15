from datetime import datetime
time = "2015-09-30 04:01"
now = "2015-12-15 21:52"
print "Time: %s, Now: %s" % (time,now)
date_format = "%Y-%m-%d %H:%M"
print "Format: %s" % date_format
now_date = datetime.strptime(now,date_format)
print now_date
time_date = datetime.strptime(time, date_format)
print time_date

print now_date > time_date
# For days. This is sickeningly easy
print (now_date - time_date).days
