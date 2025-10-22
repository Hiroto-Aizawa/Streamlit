import pandas as pd

df = pd.read_csv('./data/08_data.csv')

# 【重複の発見】
# テストデータセットを確認すると、行11と12が重複していると推測できます。
# 重複を発見するには、duplicated()メソッドを使用できます。
# duplicated()メソッドは各行に対してブール値を返します：
print(df.duplicated()) # 重複する行ごとにTrueを返し、それ以外はFalseを返す


# 【重複の削除】
# 重複を削除するには、drop_duplicates() メソッドを使用します。
df.drop_duplicates(inplace = True)
# 注意：(inplace = True) を指定すると、メソッドは新しい DataFrame を返さず、
# 元の DataFrame から重複データをすべて削除します。

print(df.to_string())