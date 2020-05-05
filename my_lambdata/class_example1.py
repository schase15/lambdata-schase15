# my_lambdata/class_example1.py

from pandas import DataFrame


def add_state_names(my_df):


    
    #  State abbreviation -> Full Name and visa versa.
    # FL -> Florida, etc.

    # Create copy of df to work with
    new_frame = my_df.copy()

    # need a list or dict with the abbrev/name mappings
    names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn', 'DC': 'District of Columbia'}

    # create a new column which maps the existing column using our names map
    # breakpoint()

    new_frame['name'] = new_frame['abbrev'].map(names_map)

    return new_frame


if __name__ == "__main__":

    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
