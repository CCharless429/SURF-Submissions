import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

dataframe = pd.read_csv("Electric_Vehicle_Population_Data.csv")
#print(dataframe.head(10))

"""
Electric_Vehicle_Population_Data.csv contains the information of vehicles registered within the state of Washington
This program filters out the data to which the data left is cars registered in King County that are
from the make NISSAN.
Then, it distributes the data on several charts using matplotlib
"""

# Creates a HISTOGRAM of number of Nissan Model Cars that are electric vehicles registered in King County, divided by model year 
king_df = dataframe[dataframe['County'] == 'King']
filter_df = king_df[king_df['Make'] == 'NISSAN']

plt.hist(filter_df['Model Year'])
plt.xlabel('Model Year')
plt.ylabel('# of Cars')
plt.title('Number of Nissan Electric Vehicles registered in King County of Washington')

# Creates a PIE CHART of the total electric vehicles registered in Washington, divided by make
makes = {}
for make in dataframe['Make']:
    if make not in makes:
        makes[make] = 1
    else:
        makes[make] += 1

makes_filtered = {}
makes_filtered['OTHER'] = 0

for make in makes.keys():
    if makes[make] <= 1000:
        makes_filtered['OTHER'] += makes[make]
        makes[make] = 0
    else:
        makes_filtered[make] = makes[make]


plt.figure(figsize = (3, 3))
plt.pie([makes_filtered[make] for make in makes_filtered], labels = makes_filtered.keys())

plt.show()



