import numpy as np
import pandas as pd

тимуры = np.array([1, 2, 3, 4, 5, 8, 4, 2, 6, 8])
print("тимуры:", тимуры)
print("тимуры среднее", тимуры.mean())
print("тимуры максимальное", тимуры.max())
print("тимуры минимальное", тимуры.min())
print(тимуры + 1)
print(тимуры * 2)

data = {
    "nickname": ['timur', 'legendatimur', 'Bybulda'],
    "group": ["1ii-2-11-26", "byblda22297", "robloxman"],
    "score": [67, 42, 89]
}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.info())
print(df.describe())

print(df["nickname"])

best = df[df["score"] >= 67]
print(best)

df["status"] = ["kill", "double kill", "triple kill"]
print(df)

df2 = pd.DataFrame({
    "nickname": ["timur", "Bybulda", None],
    "score": [67, None, 42]
})
print(df2)
print(df2.isnull().sum())
print(df2.fillna(0))