
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
diabetes_dataset = pd.read_csv("/home/tushar/Documents/MLPROJECT-1/diabetes.csv")

print(diabetes_dataset.head())
