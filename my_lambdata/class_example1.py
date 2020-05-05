# my_lambdata/class_example1.py

from pandas import DataFrame


def add_state_names(my_df):
    '''
    Converts a dataframe with a column of state abbreviations, adding a corresponding column of state names.

    Params:
        my_df a pandas.DataFrame with a column called 'abbrev'.

    Example:
        add_state_names(DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]}))

    Returns: a pandas.DataFrame with the original col as well as a "name" column.

    '''

    new_frame = my_df.copy()

    # need a list or dict with the abbrev/name mappings
    names_map = {'CA': 'Cali', 'CO': 'Colo', 
                 'CT': 'Conn', 'DC': 'District of Columbia'}

    # create a new column which maps the existing column using our names map
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    # breakpoint()

    new_frame['name'] = new_frame['abbrev'].map(names_map)

    return new_frame


if __name__ == "__main__":

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
