from functions import Scheduler
from constants import Constant
from unittest.mock import patch
from unittest import TestCase
import unittest

cte=Constant()
schl=Scheduler()
class Test(TestCase):
        
    @patch('builtins.input', return_value= "36")
    def test_file_does_not_exists(self, return_value):
        with self.assertRaises(ValueError) as context:
            next(schl.get_scheduled_workers())
        self.assertEqual(str(context.exception), cte.ERROR_FILE)
    
    @patch('builtins.input', return_value= "test_bad_format_1.txt")
    def test_bad_format_1(self, return_value):
        with self.assertRaises(ValueError) as context:
            next(schl.get_scheduled_workers())
        self.assertEqual(str(context.exception), cte.ERROR_FORMAT)
    
    @patch('builtins.input', return_value= "test_bad_format_2.txt")
    def test_bad_format_2(self, return_value):
        with self.assertRaises(ValueError) as context:
            next(schl.get_scheduled_workers())
        self.assertEqual(str(context.exception), cte.ERROR_FORMAT)
    
    @patch('builtins.input', return_value= "test_bad_format_3.txt")
    def test_bad_format_3(self, return_value):
        with self.assertRaises(ValueError) as context:
            next(schl.get_scheduled_workers())
        self.assertEqual(str(context.exception), cte.ERROR_FORMAT)
    
    @patch('builtins.input', return_value= "test_bad_format_3.txt")
    def test_bad_format_4(self, return_value):
        with self.assertRaises(ValueError) as context:
            next(schl.get_scheduled_workers())
        self.assertEqual(str(context.exception), cte.ERROR_FORMAT)

    @patch('builtins.input', return_value= "test_1.txt")
    def test_1(self, return_value):
        values=schl.get_scheduled_workers()
        self.assertEqual(next(values), "RENE-ASTRID: 2")
        self.assertEqual(next(values), "RENE-ANDRES: 2")
        self.assertEqual(next(values), "ASTRID-ANDRES: 3")
    
    @patch('builtins.input', return_value= "test_2.txt")
    def test_1(self, return_value):
        values=schl.get_scheduled_workers()
        self.assertEqual(next(values),'RENE-ASTRID: 2')
        self.assertEqual(next(values),'RENE-ANDRES: 2')
        self.assertEqual(next(values),'RENE-PEDRO: 5')
        self.assertEqual(next(values),'RENE-MARIO: 2')
        self.assertEqual(next(values),'RENE-GUS: 5')
        self.assertEqual(next(values),'RENE-ASTRIX: 2')
        self.assertEqual(next(values),'RENE-PABLO: 2')
        self.assertEqual(next(values),'RENE-KIM: 2')
        self.assertEqual(next(values),'ASTRID-ANDRES: 3')
        self.assertEqual(next(values),'ASTRID-PEDRO: 2')
        self.assertEqual(next(values),'ASTRID-MARIO: 3')
        self.assertEqual(next(values),'ASTRID-GUS: 2')
        self.assertEqual(next(values),'ASTRID-ASTRIX: 2')
        self.assertEqual(next(values),'ASTRID-PABLO: 3')
        self.assertEqual(next(values),'ASTRID-KIM: 1')
        self.assertEqual(next(values),'ANDRES-PEDRO: 2')
        self.assertEqual(next(values),'ANDRES-MARIO: 3')
        self.assertEqual(next(values),'ANDRES-GUS: 2')
        self.assertEqual(next(values),'ANDRES-ASTRIX: 2')
        self.assertEqual(next(values),'ANDRES-PABLO: 3')
        self.assertEqual(next(values),'ANDRES-KIM: 1')
        self.assertEqual(next(values),'PEDRO-MARIO: 2')
        self.assertEqual(next(values),'PEDRO-GUS: 5')
        self.assertEqual(next(values),'PEDRO-ASTRIX: 2')
        self.assertEqual(next(values),'PEDRO-PABLO: 2')
        self.assertEqual(next(values),'PEDRO-KIM: 2')
        self.assertEqual(next(values),'MARIO-GUS: 2')
        self.assertEqual(next(values),'MARIO-ASTRIX: 2')
        self.assertEqual(next(values),'MARIO-PABLO: 3')
        self.assertEqual(next(values),'MARIO-KIM: 1')
        self.assertEqual(next(values),'GUS-ASTRIX: 2')
        self.assertEqual(next(values),'GUS-PABLO: 2')
        self.assertEqual(next(values),'GUS-KIM: 2')
        self.assertEqual(next(values),'ASTRIX-PABLO: 2')
        self.assertEqual(next(values),'ASTRIX-KIM: 2')
        self.assertEqual(next(values),'PABLO-KIM: 1')

unittest.main()