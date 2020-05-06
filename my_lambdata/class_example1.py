# my_lambdata/class_example1.py

# A class example of refactoring a function into a class

from pandas import DataFrame

class Wrangler():
    '''
    Wrangler takes a dataframe and manipulates it
    '''

    # Define what is inside the class
    def __init__(self, my_df):
        '''
        Param: my_df a pandas.DataFrame with a column called 'abbrev'
        '''
        # input of my_df gets stored as self.df
        self.df = my_df

    # Define methods for class
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
        self.df['name'] = self.df['abbrev'].map(names_map)

    def inspect_columns(self):
        print(self.df.columns)


if __name__ == "__main__":

    # Run example 
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    # Initialize a new wranger object, passing our df into the class and storing it as part of 
    # the new wrangler object
    wrangler = Wrangler(df)

    # Call the inspect method
    wrangler.inspect_columns()

    # Call the addstate names method, this adds the new column to the df that is stored on the wranger object
    wrangler.add_state_names()
    
    # Print by calling the method on the df inside the wranger object
    print(wrangler.df.head())
