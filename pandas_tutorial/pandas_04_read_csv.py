import pandas as pd

df = pd.read_csv('./data/data.csv')

# to_string()メソッドを使ってDataFrame全体を表示
#print(df.to_string())

# 行数の多い大規模なDataFrameの場合、Pandasは最初の5行と最後の5行のみを表示します。
# print(df)

# 返される行数はPandasのオプション設定で定義されます。
# システムの最大行数はpd.options.display.max_rowsステートメントで確認できます。
print(pd.options.display.max_rows) # default: 60

# 私のシステムではその数は60です。つまり、DataFrameが行を60行以上含む場合、
# print(df)ステートメントはヘッダーと最初と最後の5行のみを返します。
# 同じステートメントで最大行数を変更できます。
pd.options.display.max_rows = 9999  # 最大表示行数を9999に設定
print(pd.options.display.max_rows)
print(df)