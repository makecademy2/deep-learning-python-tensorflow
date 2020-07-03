import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import datetime

# Get data
data = pd.read_csv('data/train.csv', encoding='utf-8')
print(data.head())

# Remove unwanted columns
data = data.drop(['Id', 'Alley'], axis=1)

# Separate text & numeric
data_categoric = data.select_dtypes(include=['object'])
data_categoric = pd.get_dummies(data_categoric)

data_numeric = data.select_dtypes(exclude=['object'])

# Clean
data_numeric.dropna(inplace=True)
data_categoric.dropna(inplace=True)

# Normalise
cols_to_norm = list(data_numeric.columns)

data_numeric[cols_to_norm] = data_numeric[cols_to_norm].apply(
    lambda x: (x - x.min()) / (x.max() - x.min()))

data = data_numeric.merge(data_categoric, left_index = True, right_index = True)

print(data.head())