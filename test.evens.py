import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_function_retunrs_True(self):
        self.assertTrue(even_number_of_evens([]))


unittest.main