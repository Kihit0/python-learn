import pandas as pd

df: pd.DataFrame = pd.read_csv("c:/IT/PythonProject/python-learn/tasks/task_date_0812/california_housing_train.csv")
avg: float = df[df["population"] < 500]["median_house_value"].mean()

print(avg)

minPopulation: int = df["population"].min()
max_households_in_min_population = df[df["population"] == minPopulation]["households"].max()

print(max_households_in_min_population)