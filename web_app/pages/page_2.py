import streamlit as st
import datetime


# 【フォーム】
# with句のtext_inputはbuttonが押されるまでリロードされない
# 複数の入力項目があるときにリロードの制限ができる
with st.form(key='profile_form'):
    # 【テキストボックス】
    # 戻り値:テキストボックスに入力されている値
    # データが入るタイミングは、画面がリロードされたタイミング
    # テキストボックスからカーソルが外れると戻り値に値が入る
    name = st.text_input('名前')
    adress = st.text_input('住所')
    # 【セレクトボックス】
    # 第一引数:ラベル、第二引数:選択肢のタプル
    age_category = st.selectbox(
        '年齢層',
        ('子ども(18歳未満)', '大人(18歳以上)')
    )

    # 【ボタン】
    # ボタンが押されたタイミングで値を受け取る
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    # print(f'submit_btn:{submit_btn}')
    # print(f'cancel_btn:{cancel_btn}')
    if submit_btn:
        st.text(f'ようこそ！{name}さん!\n{adress}に書類を送りました！')
        st.text(f'年齢層: {age_category}')