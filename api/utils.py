from datetime import datetime, timedelta


def add_time_interval(start_time):
    first_time = datetime(year=start_time.year, month=start_time.month, day=start_time.day, hour=8, minute=30)
    end_time = datetime(year=start_time.year, month=start_time.month, day=start_time.day, hour=17, minute=30)
    start_time = start_time + timedelta(minutes=15)
    if start_time < first_time:
        return first_time
    if start_time > end_time:
        return datetime(year=start_time.year, month=start_time.month, day=start_time.day + 1, hour=8, minute=30)
    return start_time
