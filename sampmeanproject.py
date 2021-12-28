import csv
import statistics
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
read_data=df["reading_time"].to_list()

population_mean = statistics.mean(read_data)

def random_set_of_values():
    data=[]
    for i in range(1,30):
        random_index = random.randint(0,len(read_data)-1)
        value = read_data[random_index]
        data.append(value)
    mean=statistics.mean(data)
    return mean

means=[]

for i in range(1,100):
    var = random_set_of_values()
    means.append(var)

samplemean = statistics.mean(means)
print(population_mean)
print(samplemean)

fig = ff.create_distplot([read_data], ["Reading Time"], show_hist=False)
meanfig = ff.create_distplot([means], ["Distribution of Means"], show_hist=False)
fig.show()
meanfig.show()