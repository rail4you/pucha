from datetime import datetime, timedelta
from chinese_calendar import is_workday


def add_time_interval(last_time):
    year = last_time.year
    month = last_time.month
    day = last_time.day
    begin_time = datetime(year=year, month=month, day=day, hour=8, minute=30)
    end_time = datetime(year=year, month=month, day=day, hour=17, minute=30)
    new_time = last_time + timedelta(minutes=15)
    if not is_workday(new_time):
        while not is_workday(new_time):
            new_time = new_time + timedelta(days=1)
    if new_time <= begin_time:
        new_time = begin_time
    if new_time > end_time:
        new_time = datetime(year=year, month=month, day=day + 1, hour=8, minute=30)
    return new_time
