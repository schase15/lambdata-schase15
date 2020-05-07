# Lecture notes from class 4 unit 3 sprint 1
# Going over test

# # unit test is a part of python
# import unittest


# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     unittest.main()


# A second example using enlarge function

# Define enlarge function
def enlarge(n):
        return int(n) * 100


# Create test
import unittest

class TestMyMod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(enlarge(5), 500)

if __name__ == '__main__':
    unittest.main()