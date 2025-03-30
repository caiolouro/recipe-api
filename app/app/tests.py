"""
Tests for the calculator module
"""
from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def test_add(self):
        res = calc.add(5, 5)
        self.assertEqual(res, 10)
    
    def test_subtract(self):
        res = calc.subtract(11, 15)
        self.assertEqual(res, 4)