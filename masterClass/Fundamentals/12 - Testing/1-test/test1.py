#pylint
#pyflakes
#pep.8

import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param_num = 10
        result = main.do_stuff(test_param_num)
        self.assertEqual(result, 10)

    def test_do_stuff2(self):
        test_param_num = "ghw"
        result = main.do_stuff(test_param_num)
        self.assertEqual(result, ValueError)

    def test_do_stuff3(self):
        test_param_num = 10
        result = main.do_stuff(test_param_num)
        self.assertEqual(isinstance(result, 10))

    def test_do_stuff4(self):
        test_param_num = None
        result = main.do_stuff(test_param_num)
        self.assertEqual(isinstance(result, 10))

    def test_do_stuff5(self):
        test_param_num = ''
        result = main.do_stuff(test_param_num)
        self.assertEqual(isinstance(result, 10))

#Depending on file name, checks to see if the file is diff:        
if __name__ == '__main__':
    unittest.main()