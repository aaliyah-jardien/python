import unittest

from main import add_two_numbers

class TestMyMaths(unitest.TestCase):
    def test_my_maths(self):
        self.assertEqual(add_two_numbers(2,2), 4, "Adding two numbers fai"

