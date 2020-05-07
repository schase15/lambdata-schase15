#                           UNITTEST
# 
# Testing the class that we built in class
# Testing should have its own folder, and a file for each different test
# Add information about testing in the README.md

# Create testing class
# Pass in unittest.TestCase so it inherits for that class
# Create an instance of the class we are testing
# Call a method
# Tell the test what the correct answers should be (self.assert)
# Always break it and test it again to make sure it returns a failure

# Invoke at the end with if __main__

import unittest

from my_lambdata.inheritance import WrangledFrame

class TestWrangledFrame(unittest.TestCase):

    def test_add_state_names(self):
        wf = WrangledFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

        wf.add_state_names()
        ### What are we testing?

        # ensure there is a name column
        self.assertEqual(list(wf.columns), ['abbrev', 'name'])

        # check that there are now 2 columns instead of 1
        self.assertEqual(len(list(wf.columns)), 2)

        # ensure the value of wf are specific classes/values (string, 'Cali')
        self.assertEqual(wf['name'][0], 'Cali')
        self.assertEqual(wf['abbrev'][0], 'CA')

        # self.assertEqual(test input, expected outcome)

# use unittest to run test
if __name__ == '__main__':
    unittest.main()