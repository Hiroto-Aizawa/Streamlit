# Streamlit の Tips

## docstring(ドキュメント文字列)の注意点

Streamlit の標準機能として備わっている[Magic](https://docs.streamlit.io/develop/api-reference/write-magic/magic)機能と、表示関数である st.write()の特別な挙動により、docstring(ドキュメント文字列)が Web 上に表示されるケースがあります。

【例】

```python
import streamlit as st

"""
Streamlit用のサンプルクラス
Webページに表示する内容をこのクラスに記載する
"""
class Sample:


    def calculate_sum(a, b):
        """
        引数の合計値を返す

        Args:
            a(int):
            b(int):
        """
        return a + b
```
