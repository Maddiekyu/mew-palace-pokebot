import unittest
from unittest import TestCase
from rolebot import validate_user_input

class TestRolebot(unittest.TestCase):
    def test_validate(self):
    #User entering "%sh Mimikyu" should go through.
        self.assertEqual(validate_user_input(f"%sh Mimikyu"), "found mimikyu")
        self.assertEqual(validate_user_input(f"%sh MIMIKYU"), "found mimikyu")
        self.assertEqual(validate_user_input(f"%sh mimikyu"), "found mimikyu")
        self.assertEqual(validate_user_input(f"%sh MiMiKyU"), "found mimikyu")
        self.assertEqual(validate_user_input(f"%sh Farfetch'd"), "found mimikyu")
        self.assertEqual(validate_user_input(f"%sh Kommo-o"), "found mimikyu")

    def test_troll_input(self):
    #Users who enter stupid shit should get hit.
        self.assertRaises(ValueError, validate_user_input, f"%sh bugs bunny")
        self.assertRaises(ValueError, validate_user_input, f"%sh m1m1kyu")
        self.assertRaises(ValueError, validate_user_input, f"%sh m i m i k y u")
        self.assertRaises(ValueError, validate_user_input, f"%sh maddiekyu is the best")
        self.assertRaises(ValueError, validate_user_input, f"%sh farfetchd")
        self.assertRaises(ValueError, validate_user_input, 1)
        self.assertRaises(ValueError, validate_user_input, f"%sh kommo-o")