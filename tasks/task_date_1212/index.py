import random
import pandas as pd

lst: list[str] = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
df: pd.DataFrame = pd.DataFrame({"whoAmI": lst})

uniq = df["whoAmI"].unique()

for item in uniq:
    df.loc[df["whoAmI"] == item, item] = 1
    df.loc[df["whoAmI"] != item, item] = 0
    df[item] = df[item].astype(int)

del df["whoAmI"]
print(df)