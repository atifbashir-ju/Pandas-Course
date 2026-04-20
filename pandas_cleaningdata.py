#cleaning Data: it means fixing the bad data in your data set.
#bad data could be: empty cell, data in wrong format, and wrong data.
#empty cell: it will you give wrong result alwyas, we will have to remove the rows alwyas that contain bad data

import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
print(Atif.to_string())

import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
Atifnew = Atif.dropna()
print(Atif.to_string())

#it will remove the rows containig null values
import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
Atif.dropna(inplace=True)
print(Atif.to_string())

#replacing the empty value: we will use fillna() 
import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
Atif.fillna(4, inplace=True)
print(Atif.to_string())

#to replace only the empty value for one colunm
import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
Atif["Age"].fillna(4, inplace=True)
print(Atif.to_string())

# here we can also replace the empty cell using mean() median() or mode()
import pandas as pd
Atif = pd.read_csv('dirtydata.csv')
x = Atif["Age"].mean()
Atif["Age"].fillna(x, inplace=True)
print(Atif.to_string())

