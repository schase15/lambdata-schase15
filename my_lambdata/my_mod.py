# Assignment Package
import pandas

# Define function to split dates and return into multiple columns
def date_split(X, header):
    # Convert date_recorded to datetime
    X[header] = pandas.to_datetime(X[header], infer_datetime_format=True)
    
    # Extract components from date, create new columns for each element
    X['year'] = X[header].dt.year
    X['month'] = X[header].dt.month
    X['day'] = X[header].dt.day

    return X


# Define function to turn a list into a new column on a dataframe

def list_to_column(input_list, input_df):
    # Turn given list into series
    series = pandas.Series(input_list, name='vals')
    # Turn series into a dataframe
    new_df = series.to_frame()
    # Add new dataframe as new column on input df
    input_df['new_column'] = new_df['vals']

    return input_df