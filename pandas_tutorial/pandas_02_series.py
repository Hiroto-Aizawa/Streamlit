import pandas as pd

a = [1, 7, 2]
alphabet = ["x", "y", "z"]
#myvar = pd.Series(a, index=["x", "y", "z"])
myvar = pd.Series(a, index=alphabet)

print(myvar, '\n')
#print(myvar["y"])

###
### キー/値のペアを持つ辞書からSeriesを作成
###

calories = {"day1": 420, "day2": 380, "day3": 390}

# 辞書内の2つの要素を使ってSeriesを作成
myvar2 = pd.Series(calories, index = ["day1", "day2"])

print(myvar2, '\n')

###
### Data Frameの作成
###

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df, '\n')