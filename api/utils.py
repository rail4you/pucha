from datetime import datetime, timedelta
from itertools import chain

from django.db.models import Q

from api.models import TimeSheet, CheckProject


def add_time_interval(start_time):
    first_time = datetime(year=start_time.year, month=start_time.month, day=start_time.day, hour=8, minute=30)
    end_time = datetime(year=start_time.year, month=start_time.month, day=start_time.day, hour=17, minute=30)
    start_time = start_time + timedelta(minutes=15)
    if start_time < first_time:
        return first_time
    if start_time > end_time:
        return datetime(year=start_time.year, month=start_time.month, day=start_time.day + 1, hour=8, minute=30)
    return start_time


def first_available_date(time):
    day = time.day
    print(day)
    am_pm = time.strftime("%p")
    # time >= time and ((am > 0) or (pm > 0))
    result = TimeSheet.objects.filter(Q(is_holiday=False), Q(time__gte=time), Q(am__gt=0) | Q(pm__gt=0))
    if not result:
        return "None"
    timesheet = result.first()
    if timesheet.am > 0:
        return (timesheet.time, "am")
    else:
        return (timesheet.time, "pm")


def create_time_sheet(check_project_id):
    check_project = CheckProject.objects.get(pk=check_project_id)
    start_time = check_project.start_time
    end_time = check_project.end_time

    for n in range(int((end_time - start_time).days) + 1):
        current_date = start_time.date() + timedelta(n)
        TimeSheet.objects.create(check_project=check_project, time=current_date)


def select_item(timesheet):
    result = []
    if timesheet.am > 0 :
        result.append({"date":timesheet.time, "time_part":"am"})
    if timesheet.pm >0:
        result.append({"date":timesheet.time, "time_part":"am"})
    return result

def create_available_date_range(time):
    result = TimeSheet.objects.filter(Q(is_holiday=False), Q(time__gte=time), Q(am__gt=0) | Q(pm__gt=0))

    return list(chain(*[select_item(item) for item in result]))


def get_paginated_list(items, page, limit):
    '''
        Custom pagination for any list.
        items = array/list
        page = current page number
        limit = number of items to be shown on page
    '''
    obj = {}

    count = len(items)

    obj['limit'] = limit

    if count <= limit:
        total_pages = 1
        limit = count
    else:
        total_pages = count / limit;

    start = (page - 1) * limit
    end = start + limit

    if end > count:
        end = count

    if page > total_pages or page <= 0:
        return  # handle 404 error page

    obj['current_page'] = page
    obj['total_item_count'] = count
    obj['total_pages'] = total_pages

    if page == 1:
        obj['previous'] = ''
        obj['has_previous'] = False
    else:
        obj['previous'] = page - 1
        obj['has_previous'] = True

    if page >= total_pages:
        obj['next'] = ''
        obj['has_next'] = False
    else:
        obj['next'] = page + 1
        obj['has_next'] = True

    obj['items'] = items[start:end]
    return obj
create_available_date_range(datetime.today())