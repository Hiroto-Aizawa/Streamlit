import streamlit as st
import pandas as pd

st.markdown('# データ分析アプリ')

code = '''
import streamlit as st

st.title('ファイルをアップロードしてデータ分析')
'''

st.code(code, language='python')

uploaded_file = st.file_uploader('CSVファイルをアップロードしてください', type=['csv'])
if uploaded_file is not None:
    st.info('ファイルがアップロードされました。')

    df = pd.read_csv(uploaded_file)
    st.write('データのプレビュー:')
    st.dataframe(df.head(5)) # 先頭5行だけ表示

    column_names = [c for c in df.columns]
    target_column = st.selectbox(
        'ターゲットを選択してください', 
        column_names
    )
    st.info(f'{target_column}を予測対象として予測モデルを作ります！')
    # if st.button('基本統計量を表示'):
    #     st.write('基本統計量:')
    #     st.write(df.describe())