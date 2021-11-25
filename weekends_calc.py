#!/usr/bin/env python3

import datetime
import calendar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

current_year = datetime.datetime.now().year
start_work_day = datetime.date(current_year, 11, 22)
weekend = datetime.timedelta(days=4) + start_work_day
day_of_week = weekend.isoweekday()
calendar_month = calendar.TextCalendar(calendar.SUNDAY)

if day_of_week != 6:
    while day_of_week != 6:
        next_day_postition = weekend + datetime.timedelta(days=6)
        day_of_week = next_day_postition.isoweekday()
        if day_of_week != 6:
            weekend = next_day_postition
    print(f"{bcolors.WARNING}{next_day_postition}{bcolors.ENDC}")
    c_str = calendar_month.formatmonth(next_day_postition.year,next_day_postition.month)
    print(f"{bcolors.OKGREEN}{c_str}{bcolors.ENDC}")
elif day_of_week == 6:
    print(f"{bcolors.WARNING}{weekend}{bcolors.ENDC}")
    c_str = calendar_month.formatmonth(weekend.year,weekend.month)
    print(f"{bcolors.OKCYAN}{c_str}{bcolors.ENDC}")