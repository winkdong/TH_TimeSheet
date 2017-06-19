### ref: http://pbpython.com/excel-file-combine.html

## Collecting the Data
import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob("../in/*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

all_data.describe()
### the best practice is to convert the data column to a date time object.
all_data['date'] = pd.to_datetime(all_data['date'])

## Combining the Data
## like the join function in ArcGIS Table

status = pd.read("../custom-status.xlxs")
status

all_data_st = pd.merge(all_data,status,how='left') #like Excel's vlookup
all_data_st.head()

all_data_st['status'].fillna('bronze',implace=True)
all_data_st.head()


## Using Categories
all_data_st["status"] = all_data_st["status"].astype("category")
all_data_st.head()
all_data_st.dtypes

all_data_st.sort(columns=["status"]).head()

all_data_st["status"].cat.set_categories(["gold","silver","bronze"],inplace=True)
all_data_st.sort(columns=["status"]).head()


