# Practicing creating an inheritance class from my own example

import pandas

from my_lambdata.assignment import Date

# Create child from parent class of Date

class NewDate(Date):
    '''
    Takes attributes and methods from Date class, adds a method to 
    convert numeric months to string names
    '''

    def month_name(self):
        # map numeric months to names
        month_map = {4: 'April', 5: 'May'}

        self.df['month'] = self.df['month'].map(month_map)

if __name__ == "__main__":
    
    # Use Date class to split into columns

    # Define attributes
    z = pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
        '5/30/2010']})

    # Create object
    date_df = NewDate(z, 'date')

    # Call method - this will modify the df stored inside the object
    date_df.split()

    # Print df inside object
    print(date_df.df)

    # Call new method to convert numeric months to string names
    date_df.month_name()

    print(date_df.df)
