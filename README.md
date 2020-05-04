# lambdata-schase15

## Installation
```sh
pip install -i https://test.pypi.org/simple/ lambdata-schase15==1.2
```

## Usage

```py
import pandas as pd
from my_lambdata.my_mod import date_split, list_to_column

date_split(df, 'column_header_with_date_to_split')

list_to_column(input_list, input_df)

```

## Notes
For date_split:
Make sure you are including quotations around the column header name that includes the dates you want to split.

Make sure pandas is imported as pd