import sqlite3
import unittest
from datetime import datetime
from database import Database
from calculator import *

class Test(unittest.TestCase):
    # Positive testes
    def test_ticket_id_1(self):
        self.assertEqual(calculate_sum("1"), 750.0)

    def test_ticket_id_11(self):
        self.assertEqual(calculate_sum("11"), 225.0)

    def test_ticket_id_26(self):
        self.assertEqual(calculate_sum("26"), 150.0)

    def test_ticket_id_30(self):
        self.assertEqual(calculate_sum("30"), 150.0)

    def test_ticket_id_17(self):
        self.assertEqual(calculate_sum("17"), 500.0)

    # Negative testes
    def test_ticket_id_3(self):
        self.assertEqual(calculate_sum("3"), "Error: you can't return an unpurchased ticket!")

    def test_ticket_negative_id(self):
        self.assertEqual(calculate_sum("-999"), "Error: can't find the ticket!")

    def test_ticket_big_id(self):
        self.assertEqual(calculate_sum("9999999"), "Error: can't find the ticket!")

    def test_ticket_string_id(self):
        self.assertEqual(calculate_sum("HELLO, WORLD!"), "Error: can't find the ticket!")

    def test_ticket_string_id_2(self):
        self.assertEqual(calculate_sum("третий билет"), "Error: can't find the ticket!")


if __name__ == '__main__':
    unittest.main()
    
