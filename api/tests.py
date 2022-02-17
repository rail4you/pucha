# from django.test import TestCase

# Create your tests here.
from datetime import datetime
import pytest
from api.utils import add_time_interval
import requests

def test_add_time_inteval():
    time = datetime(2022, 3, 1, 8, 30)
    assert add_time_interval(time) == datetime(2022, 3, 1, 8, 45)

def test_hello_api():
    pass