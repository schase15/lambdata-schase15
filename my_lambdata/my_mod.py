# def enlarge(n):
#     return int(n) * 100

# if __name__ == "__main__":
#     # only run the following code
#     # when we run this script from the command-line
#     # otherwise don't invoke this code (for example when importing from another file)

#     x=5
#     print(enlarge(x))

#     z= input('Please choose a number to enlarge:')
#     print(enlarge(int(z)))


# Assignment Package
import pandas

# Define function to split dates and return into multiple columns
def date_split(X['date']):
    # Convert date_recorded to datetime
    X['date'] = pandas.to_datetime(X['date'], infer_datetime_format=True)
    
    # Extract components from date, create new columns for each element
    X['year'] = X['date'].dt.year
    X['month'] = X['date'].dt.month
    X['day'] = X['date'].dt.day

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