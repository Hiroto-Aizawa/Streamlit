import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df)
# print(df2)

# ### 行の検索
# print(df.loc[0])  # インデックス0の行を取得
# print(df.loc[[0, 1]])  # インデックス0と1の行を取得
# print(df2.loc["day2"])


### ファイルをDataFrameに読み込む

df3 = pd.read_csv('./data/data.csv')
print(df3)