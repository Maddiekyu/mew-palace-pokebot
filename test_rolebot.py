import unittest
from unittest import TestCase
from rolebot import validate_user_input

class TestRolebot(unittest.TestCase):
    def test_validate(self):
    #User entering "%sh Mimikyu" should go through.
        self.assertEqual(validate_user_input(f"%sh Mimikyu"), "found Mimikyu")
        self.assertEqual(validate_user_input(f"%sh Mimikyu"), "found Mimikyu")
        self.assertEqual(validate_user_input(f"%sh Mimikyu"), "found Mimikyu")
        self.assertEqual(validate_user_input(f"%sh Mimikyu"), "found Mimikyu")

    def test_troll_input(self):
    #Users who enter garbage should get rejected, idiot.
        self.assertRaises(ValueError, validate_user_input, f"%sh bugs bunny")
        self.assertRaises(ValueError, validate_user_input, f"%sh m1m1kyu")
        self.assertRaises(ValueError, validate_user_input, f"%sh m i m i k y u")
        self.assertRaises(ValueError, validate_user_input, f"%sh maddiekyu is the best")