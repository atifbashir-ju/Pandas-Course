#read csv files: (comma seprated value or file) it is a simple way to store the big data and biggest data

#loading the csv into a dataframe with to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

#loading the csv into a dataframe without to_string
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

#max rows: you can check your system's maximum rows with:

import pandas as pd
print(pd.options.display.max_rows)


#we can increase the maximum no of rows to display entire data frame
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)