import pandas as pd

df = pd.read_csv('./data/08_data.csv')

# 【行の削除】
# 空のセルに対処する一つの方法は、空のセルを含む行を削除することです。
# データセットは非常に大規模になる可能性があるため、通常は問題ありません。
# 数行を削除しても結果に大きな影響を与えません。

# デフォルトでは、dropna()メソッドは新しいDataFrameを返すため、元のDataFrameは変更されません。
new_df = df.dropna()

# 元のDataFrameを変更したい場合は、inplace=True引数を使用します。
df.dropna(inplace=True)

print(new_df.to_string())
print(df.to_string())

print(df)

# 【空の値を置換する】
# 空のセルを扱う別の方法は、代わりに新しい値を挿入することです。
# この方法なら、空のセルがいくつかあるからといって行全体を削除する必要はありません。
# fillna()メソッドを使えば、空のセルを値で置き換えることができます
# nullの値を130に書き変える
df.fillna(130, inplace = True)

print(df)


# 【指定された列のみ置換】
# 上記の例は、データフレーム全体の空のセルをすべて置換します。
# 特定の列の空の値のみを置換するには、データフレームに対して列名を指定します。
# 「Calories」列の空のセルを130に置き換える
df.fillna({"Calories": 130}, inplace = True)

print(df)

# 【平均、中央値、または最頻値を使用して置換する】
# 空のセルを置き換える一般的な方法は、列の平均値、中央値、または最頻値を計算することです。
# Pandasでは、指定した列のそれぞれの値を計算するために、
# mean()、median()、mode()メソッドを使用します：

# 平均値を計算し、空の値がある場合はその値で置き換える：
x = df["Calories"].mean()

# 中央値を計算し、空の値があればそれに置き換える：
x = df["Calories"].median()

# 最頻値を計算し、空の値があればそれに置き換える：
x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace = True)