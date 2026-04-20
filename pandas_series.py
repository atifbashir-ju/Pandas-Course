#A pandas series is like a colunm in a table. it is 1-D array which holds data of any type

import pandas as pd
Atif = [1, 7, 2]
Atifnew = pd.Series(Atif)
print(Atifnew)
#labeling- it can be used to access a specified value
import pandas as pd
Atif = [1, 7, 2]
Atifnew = pd.Series(Atif)
print(Atifnew[0])

import pandas as pd
Atif = [1, 7, 2]
Atifnew = pd.Series(Atif, index = ["x", "y", "z"])
print(Atifnew['x'])


import pandas as pd
cal = {"day1": 420, "day2": 380, "day3": 390}
Atifnew = pd.Series(cal)
print(Atifnew)