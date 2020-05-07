# my_lambdata/inheritance.py

# A class example of using inheritance

from pandas import DataFrame

# Passing in the class DataFrame as this is an inheritance example,
# Our class will inherit everything from its parent class and then we will modify it
class WrangledFrame(DataFrame):
    '''
    A custom pandas.DataFrame with a column called "abbrev"

    Example: WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    '''

    def add_state_names(self):
        '''
        Converts a dataframe with a column of state abbreviations, adding a corresponding column of state names.

        Returns: a pandas.DataFrame with the original col as well as a "name" column.

        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        '''

        # need a list or dict with the abbrev/name mappings
        names_map = {'CA': 'Cali', 'CO': 'Colo', 
                    'CT': 'Conn', 'DC': 'District of Columbia'}

        # create a new column which maps the existing column using our names map
        self['name'] = self['abbrev'].map(names_map)

    def inspect_columns(self):
        print(self.columns)


if __name__ == "__main__":

# Since we are inheriting from the DataFrame class we can use its methods: ex df.head()

# Instantiate a new object using our class
    wf = WrangledFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(wf.head())

# Call the add state names method to our new class
    wf.add_state_names()
    print(wf.head())

# Call the inspect method to our new class
    wf.inspect_columns
