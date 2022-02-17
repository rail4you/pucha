# from django.test import TestCase

import pytest
import requests
# Create your tests here.
from datetime import datetime

from api.utils import add_time_interval


def test_add_time_interval():
    time = datetime(2022, 3, 1, 8, 30)
    assert add_time_interval(time) == datetime(2022, 3, 1, 8, 45)


def test_hello_api():
    pass
