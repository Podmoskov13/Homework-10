import pandas as pd
import random
lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI":lst})

categories = {}
for i in data["whoAmI"].unique():
    categories[i] = len(categories)
one_hot_data = pd.DataFrame(0, columns=categories.keys(), index=range(len(data)))

for i, category in enumerate(data["whoAmI"]):
    one_hot_data.loc[i, category] = 1
result = pd.concat([data, one_hot_data], axis=1).drop("whoAmI", axis=1)
print(result.head())