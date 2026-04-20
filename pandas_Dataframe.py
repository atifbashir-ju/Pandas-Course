#Data frame: it is a 2-D data structure like a 2d array
import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data)
print(Atif)

#locate row: panads use the loc to return or more specified row
import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data)
print(Atif.loc[2])

import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data)
print(Atif.loc[[0, 1]])

#named index: with the index arg, you can name your own index.
import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(Atif)



import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(Atif.loc["day3"])



import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(Atif.loc[["day1", "day2"]])


#load the csv file into data frame
import pandas as pd
fileload = pd.read_csv('data.csv')
print(fileload)
