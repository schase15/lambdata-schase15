# Assignment Package
# Create a package that includes two helper functions
# Transform one of the helper functions into a class
# Make sure they run on the terminal
# Push them to TestPyPI

import pandas

# Define function to split dates and return into multiple columns
def date_split(X, header):
    '''
    Converts a dataframe with a column of dates, adding corresponding columns
    of year, month and day.

    Params:
        X: a pandas.DataFrame with a column including dates.
        header: the column header to split into year, month, day. Must include
        quotations around column header name.

    Example:
        date_split(pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
        '5/30/2020']}), 'date')

    Returns: a pandas.DataFrame with the original columns as well as a column
            for 'year', 'month', and 'day'.

    '''
    # Convert date_recorded to datetime
    X[header] = pandas.to_datetime(X[header], infer_datetime_format=True)

    # Extract components from date, create new columns for each element
    X['year'] = X[header].dt.year
    X['month'] = X[header].dt.month
    X['day'] = X[header].dt.day

    return X


### Also coverted the first function into a class
class Date():
    '''
    Takes a df with a date column and splits it into seperate year, month, day columns.
    Keeps the original column.
    '''

    def __init__(self, df, header):
        self.df = df
        self.name = header
        '''
        Params: pandas.Dataframe with a date column
                header of column containing dates. Must be a string.
        '''

    def split(self):
        '''
        Splits given date column into year, month and day and adds them back to the original dataframe as new columns
        '''

    # Converts to datetime
        self.df[self.name]   = pandas.to_datetime(self.df[self.name], infer_datetime_format=True)

    # Extract components from date, create new columns for each element
        self.df['year'] = self.df[self.name].dt.year
        self.df['month'] = self.df[self.name].dt.month
        self.df['day'] = self.df[self.name].dt.day



# Create a new class called: NewSeries
class NewSeries():
    '''
    Takes in a list and adds it to an existing pandas.Dataframe
    '''

    def __init__(self, input_list, input_df):
        '''
        Params: input_list a list to be converted into a column. Takes floats, integers or strings
                input_df an existing pandas.DataFrame that you want to add the new column to
        '''

    # Parameters
        self.list = input_list
        self.df = input_df

    # Method: converts input_list to a column
    def to_column(self):
        '''
        Takes the given list and adds it as a column to a given pandas.DataFrame
        '''

        x = pandas.Series(self.list, name='vals').to_frame()
        self.df['new_column'] = x['vals']


# If you are calling to this page directly from the terminal it will run the code below
# Used to test your functions
# You can create another page and import these functions and dictate the input values
# and it will run only the above codes to execute your script

if __name__ == "__main__":
    
# Use NewSeries class to convert list to column and add to df
    input_list= [10, 11, 12]
    input_df= pandas.DataFrame({'col1': [1, 2, 3],
                                'col2': [4, 5, 6]})

    # Instantiate the class
    new_df= NewSeries(input_list, input_df)

    # Call method
    new_df.to_column()

    # View resulting df
    print(new_df.df)


# Use date_split function
    X = pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
        '5/30/2010']})

    print(date_split(X, 'date'))

# Use Date class to split into columns

    # Define attributes
    z = pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
        '5/30/2010']})

    # Create object
    date_df = Date(z, 'date')

    # Call method - this will modify the df stored inside the object
    date_df.split()

    # Print df inside object
    print(date_df.df)
