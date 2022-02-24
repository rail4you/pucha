# from django.test import TestCase

# Create your tests here.
from datetime import datetime

from api.utils import add_time_interval
from api.utils import last_available_date


def test_add_time_inteval():
    time = datetime(2022, 3, 1, 8, 30)
    assert add_time_interval(time) == datetime(2022, 3, 1, 8, 45)


def test_hello_api():
    pass


def test_date():
    assert last_available_date(datetime.today()) == "2022-2-20"
