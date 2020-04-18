#Project Mercuri

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dss.csv')
X = dataset.iloc[:-1, :].values

#Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:-1, :-1] = labelencoder_X.fit_transform(X[:-1, :-1])

