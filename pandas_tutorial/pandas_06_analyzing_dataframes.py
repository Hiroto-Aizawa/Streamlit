import pandas as pd

###
### Viewing th Data
###
df = pd.read_csv('./data/data.csv')

# head()メソッドは、ヘッダーと指定された行数を、先頭から返します。
print(df.head(10)) # 先頭10行を表示

# 行数が指定されていない場合、head()メソッドは上位5行を返します。
print(df.head())


# tail()メソッドは、ヘッダーと指定された行数を、末尾から順に返します。
# 行数の指定がない場合は、tail()メソッドは末尾の5行を返します。
print(df.tail())


###
### データに関する情報
###

# DataFramesオブジェクトにはinfo()というメソッドがあり、
# データセットに関する詳細情報を取得できます。
print(df.info())

# 実行結果例:
#  <class 'pandas.core.frame.DataFrame'>
#   RangeIndex: 169 entries, 0 to 168
#   Data columns (total 4 columns):

#    #   Column    Non-Null Count  Dtype  
#   ---  ------    --------------  -----  
#    0   Duration  169 non-null    int64  
#    1   Pulse     169 non-null    int64  
#    2   Maxpulse  169 non-null    int64  
#    3   Calories  164 non-null    float64
#   dtypes: float64(1), int64(3)
#   memory usage: 5.4 KB
#   None

# 169行、4列のデータセットであることがわかります。
# また、各列のデータ型と、各列に存在する非NULL値の数もわかります。
# Calories列には5つのNULL値が含まれていることがわかります。