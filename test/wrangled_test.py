# Using pytest
# Don't need self
# Don't need to create a class

# Testing the class that we built in class
# Testing should have its own folder, and a file for each different test
# Add information about testing in the README.md

from my_lambdata.inheritance import WrangledFrame

def test_add_state_names():
    wf = WrangledFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})

    wf.add_state_names()
    ### What are we testing?

    # ensure there is a name column
    assert list(wf.columns) == ['abbrev', 'name']

    # check that there are now 2 columns instead of 1
    # self.assertEqual(len(list(wf.columns)), 2)

    # ensure the value of wf are specific classes/values (string, 'Cali')
    assert wf['name'][0] == 'Cali'
    assert wf['abbrev'][0] == 'CA'

