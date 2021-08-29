import unittest

import main_functions

"""
don't care so much about the DRY
READABILITY is focused

Add comment
"""
class TestMainFunctions(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main_functions.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'abc'
        # result = main_functions.do_stuff(test_param)
        # self.assertEqual(result, ValueError)
        # self.assertIsInstance(result, ValueError)
        with self.assertRaises(ValueError) as error:
            main_functions.do_stuff(test_param)
            self.assertEqual(error.exception.message,  "invalid literal for int() with base 10: 'abc'")

    def test_do_stuff3(self):
        test_param = None
        result = main_functions.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main_functions.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest()
