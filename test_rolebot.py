import unittest
from unittest import TestCase
from rolebot import validate_user_input

class TestRolebot(unittest.TestCase):
    def test_validate(self):
    #User entering "%sh Mimikyu" should go through.
        self.assertEqual(validate_user_input("%sh Mimikyu"), "found mimikyu")
        self.assertEqual(validate_user_input("%sh MIMIKYU"), "found mimikyu")
        self.assertEqual(validate_user_input("%sh mimikyu"), "found mimikyu")
        self.assertEqual(validate_user_input("%sh MiMiKyU"), "found mimikyu")

    def test_troll_input(self):
    #Users who enter garbage should get rejected, idiot.
        self.assertRaises(ValueError, validate_user_input, "%sh bugs bunny")
        self.assertRaises(ValueError, validate_user_input, "%sh m1m1kyu")
        self.assertRaises(ValueError, validate_user_input, "%sh m i m i k y u")
        self.assertRaises(ValueError, validate_user_input, "%sh maddiekyu is the best")