import pandas as pd

df = pd.read_csv('./data/08_data.csv')

# 【行の削除】
# 空のセルに対処する一つの方法は、空のセルを含む行を削除することです。
# データセットは非常に大規模になる可能性があるため、通常は問題ありません。
# 数行を削除しても結果に大きな影響を与えません。

# デフォルトでは、dropna()メソッドは新しいDataFrameを返すため、元のDataFrameは変更されません。
# new_df = df.dropna()

# 元のDataFrameを変更したい場合は、inplace=True引数を使用します。
df.dropna(inplace=True)

# print(new_df.to_string())
print(df.to_string())

print(df)