# lambdata-schase15

## Installation
```sh
pip install -i https://test.pypi.org/simple/ lambdata-schase15==1.6
```

## Usage

```py
import pandas
from my_lambdata.my_mod import date_split, list_to_column

date_split(df, 'column_header_with_date_to_split')

list_to_column(input_list, input_df)

```

## Documentation

    '''
    date_split(X, header):

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

    '''
    list_to_column(input_list, input_df):

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