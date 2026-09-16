
import pandas as pd

df=pd.read_csv(r"D:\Vendor Details\Manish\DA - Assignments\Python\Panda\titanic.csv")

columns = ["Age", "Fare", "SibSp", "Parch"]

summary = pd.DataFrame({
    "Mean": df[columns].mean(),
    "Median": df[columns].median(),
    "Mode": df[columns].mode().iloc[0],
    "Std Dev": df[columns].std(),
    "25th Percentile": df[columns].quantile(0.25),
    "50th Percentile": df[columns].quantile(0.50),
    "75th Percentile": df[columns].quantile(0.75)
})

print(summary)