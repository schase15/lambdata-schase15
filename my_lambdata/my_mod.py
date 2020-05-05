# Assignment Package
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


# Define function to turn a list into a new column on a dataframe

def list_to_column(input_list, input_df):
    '''
    Converts a given list into a column and then adds it to a given
    pandas.DataFrame.

    Params:
        input_list: a list to be added as a column to pandas.DataFrame.
        input_df: an existing pandas.DataFrame that you want to add the list to

    Example:
        list_to_column([7, 8, 9], pandas.DataFrame({'col1': [1, 2, 3],
                                                    'col2': [4, 5, 6]}))

    Returns: a pandas.DataFrame with the original columns as well as a new
            column named new_column with values from given list.

    '''
    # Turn given list into series
    series = pandas.Series(input_list, name='vals')
    # Turn series into a dataframe
    new_df = series.to_frame()
    # Add new dataframe as new column on input df
    input_df['new_column'] = new_df['vals']

    return input_df
