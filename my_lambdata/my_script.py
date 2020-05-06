import pandas

# Import package I created on my_mod.py page
from my_lambdata.my_mod import list_to_column

# Testing working with terminal commands
print("Hello World")

print(2+2)

# Testing calling mod and inputing values
input_df = pandas.DataFrame({"a":[1,2,3], "b":[4,5,6]})

input_list= [7, 8, 9]

print(list_to_column(input_list, input_df))

print(input_df['a'])