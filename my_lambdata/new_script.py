# Testing new things out
# Writing my own script

import pandas

# from my_lambdata.assignment import date_split

# print(date_split(pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
#         '5/30/2020']}), 'date'))

from my_lambdata.assignment import NewSeries

z = pandas.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7,8]})

column = NewSeries([9, 10, 11, 12], z)

column.to_column()

print(column.df)



from my_lambdata.practice_inheritance import NewDate

df= pandas.DataFrame({'date': ['4/25/2017', '5/5/2018',
    '5/30/2020']})

date = NewDate(df, 'date')

print(date.df)

