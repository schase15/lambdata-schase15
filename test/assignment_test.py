# Creating test for assignment

# Using unittest
import unittest

# Using function I created on assignment.py
from my_lambdata.assignment import Date

# Function itself uses pandas so I need to import that
import pandas


class TestDate(unittest.TestCase):
    def test_date(self):

        # Create instance of object - saves df and header inside object
        date = Date(pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
                    '5/30/2010']}), 'date')

        # Call method on instance - performs function and modifies df stored
        # in object
        date.split()

        # What are we testing
        # Column headers on resulting df should read date, year, month, day
        self.assertEqual(list(date.df.columns), ['date', 'year', 'month',
                                                 'day'])


# use unittest to run test in terminal with
# python -m test.assignment_test
if __name__ == '__main__':
    unittest.main()
