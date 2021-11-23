import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

data_mean=statistics.mean(data)
data_sd=statistics.stdev(data)

def show_fig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([data],["claps"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def randomMeanSet(counter):
    dataset=[]
    for i in range (0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    meanList=[]
    for i in range (0,1000):
        setOfMeans=randomMeanSet(100)
        meanList.append(setOfMeans)
    show_fig(meanList)
    themean=statistics.mean(meanList)
    print("The mean is: ",themean)

setup()
totalMean=statistics.mean(data)
print("The total mean is: "+totalMean)
