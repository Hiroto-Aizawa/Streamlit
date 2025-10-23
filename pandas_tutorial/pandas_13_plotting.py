import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/13_data.csv')

# 【プロット作成】
# Pandasはplot()メソッドを使用して図を作成します。
# MatplotlibライブラリのサブモジュールであるPyplotを使用することで、図を画面上に可視化できます。
df.plot()
plt.show()

# 【散布図】
# kind引数で散布図を指定します：
# kind = 'scatter'

# 散布図にはx軸とy軸が必要です。
# 以下の例では、x軸に「Duration」、y軸に「Calories」を使用します。
# xとy引数を次のように指定します：
# x = 'Duration', y = 'Calories'
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
# 前の例では、「Duration（持続時間）」と「Calories（消費カロリー）」の相関係数が0.922721
# であることを学び、持続時間が長いほど消費カロリーが増えるという結論に至りました。


# 別の散布図を作成しましょう。ここでは「Duration」と「Maxpulse」のように、
# 列間の相関関係が非常に弱い（相関係数 0.009403）ケースを扱います：
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

# 【ヒストグラム】
# ヒストグラムを作成するには kind 引数を使用します:
# kind = 'hist'
# ヒストグラムは1列のみで作成できます。
# ヒストグラムは各区間の頻度を示します。例えば、50分から60分の間だったワークアウトは何件あったか？
# 以下の例では「Duration」列を使用してヒストグラムを作成します:
df['Duration'].plot(kind = 'hist')
plt.show()
# ヒストグラムは、50分から60分の間続いたワークアウトが100回以上あったことを示しています。