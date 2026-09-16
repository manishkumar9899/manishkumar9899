
import pandas as pd

df=pd.read_csv(r"D:\Vendor Details\Manish\DA - Assignments\Python\Panda\titanic.csv")

# print(df.head())

# print(df.describe())

# columns = ["Age", "Fare", "SibSp", "Parch"]

# print(df[columns].describe())

# print(df["Age"].mode())

# print(df["Age"].quantile(0.25))
# print(df["Age"].quantile(0.50))
# print(df["Age"].quantile(0.75))

print(df["Fare"].quantile([0.25, 0.50, 0.75]))