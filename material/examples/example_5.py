import unittest


def my_add_function(x, y):
    return x + y


class MyAddFunctionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(7, my_add_function(3,4))
        self.assertEqual(8, my_add_function(3,4))

if __name__ == '__main__':
    unittest.main()
