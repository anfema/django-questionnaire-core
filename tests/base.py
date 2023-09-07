from django.test import TestCase


# Create your tests here.
class TestCaseBase(TestCase):
    fixtures = ("test1.json",)
