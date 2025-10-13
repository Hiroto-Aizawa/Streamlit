import streamlit as st

st.markdown('# データ分析アプリ')

code = '''
import streamlit as st

st.title('ファイルをアップロードしてデータ分析')
'''

st.code(code, language='python')

uploaded_file = st.file_uploader('CSVファイルをアップロードしてください', type=['csv'])
if uploaded_file is not None:
    import pandas as pd

    df = pd.read_csv(uploaded_file)
    st.write('データのプレビュー:')
    st.dataframe(df.head())

    if st.button('基本統計量を表示'):
        st.write('基本統計量:')
        st.write(df.describe())