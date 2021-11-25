#!/usr/bin/env python3

import datetime

current_year = datetime.datetime.now().year
start_work_day = datetime.date(current_year, 11, 22)
weekend = datetime.timedelta(days=4) + start_work_day
day_of_week = weekend.isoweekday()

if day_of_week != 6:
    while day_of_week != 6:
        next_day_postition = weekend + datetime.timedelta(days=6)
        day_of_week = next_day_postition.isoweekday()
        if day_of_week != 6:
            weekend = next_day_postition
    print(next_day_postition)
elif day_of_week == 6:
    print(weekend)

# print(start_work_day)
#print(weekend)
#print(day_of_week)