#!/usr/bin/env python3

import datetime

currentYear = datetime.datetime.now().year

start_work_day = datetime.date(currentYear, 11, 22)

weekend = datetime.timedelta(days=4) + start_work_day

day_of_week = weekend.isoweekday()




print(start_work_day)
print(weekend)
print(day_of_week)