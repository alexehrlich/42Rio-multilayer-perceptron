import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data.csv", header=None)

#Drop the ID column, since it is not necessary for the training
df = df.drop(columns=[0])

print("---Count of target in data set---")
print(df[1].value_counts())
print("---------------------------------\n")

#Encode the categorial values M and B to 1 and 0
df[1] = df[1].map({'M': 1, 'B': 0})

#1. Impute missing in each column with the mean of that column
#2. Standardize the values with mean and standard deviation
for i in range(2, 31):
    #replace all 0 with a Nan value to calc the mean of each column without 0
    df[i] = df[i].replace(to_replace=0, value=np.nan)
    mean = df[i].mean()
    std = df[i].std()
    df[i] = df[i].replace(to_replace=np.nan, value=mean)

    #Standardizing the values.
    #With this step the imputed values are ofc 0 again, since we set tem to be the mean
    #and here we subtract the mean. Now they are centered.
    df[i] = (df[i] - mean)/std

print(df)