import pandas as pd
data = {"cal":[420, 345, 569], "duration":[50, 40, 45]}
Atif = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(Atif.loc[["day1", "day2"]])
