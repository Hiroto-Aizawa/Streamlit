import pandas as pd

# 【不正な形式のデータ】
# 不正な形式のデータを含むセルは、データの分析を困難にしたり、
# 場合によっては不可能にしたりする可能性があります。
# 修正するには、次の2つの方法があります：
# 行を削除するか、列内のすべてのセルを同じ形式に変換します。


# 【正しい形式に変換する】
# 「日付」列の全セルを日付に変換してみましょう。
# Pandasにはこのための to_datetime() メソッドがあります：
df = pd.read_csv('./data/08_data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

# 結果からわかるように、26行目の日付は修正されましたが、
# 22行目の空欄の日付にはNaT（Not a Time）値、つまり空の値が割り当てられました。
# 空の値に対処する一つの方法は、該当行全体を削除することです。

# 【行の削除】
# 上記の変換結果から得られたNaT値はNULL値として扱えるため、
# dropna()メソッドを使用して行を削除できます。
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())