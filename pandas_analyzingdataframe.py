# viewing the data: one of the most method for quick overview of the dataframe is the head() method

import pandas as pd
Atif = pd.read_csv('data.csv')
print(Atif.head(10))


import pandas as pd
Atif = pd.read_csv('data.csv')
print(Atif.tail(10))


#what if you want the information about the data in the dataframe: via info()
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())

