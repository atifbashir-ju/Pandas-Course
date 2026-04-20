#JSON: Big data sets are normally stored and extracted as json.

import pandas as pd
Atif = pd.read_json('data.json')
print(Atif.to_string())

#if your json code is not in a file but in a python dictionary.
import pandas as pd
data = {
  "company": "TechNova",
  "generated_on": "2026-04-20",
  "employees": [
    {
      "id": 101,
      "name": "Atif Bashir",
      "age": 22,
      "department": "Data Science",
      "skills": ["Python", "Machine Learning", "Pandas", "NumPy"],
      "salary": 75000
    }
  ]
}
Atifnew= pd.DataFrame(data)
print(Atifnew)