import streamlit as st
from PIL import Image
import datetime

st.title('サンプルアプリ')
st.caption('これはテストアプリです')
st.subheader('サブヘッダー')
st.text('これはテキストです\nここからは改行されます')

code = '''
import streamlit as st

st.title('サンプルアプリ')
'''

st.code(code, language='python')

# 【画像】
image = Image.open('Git_DL_page.png')
st.image(image, width=200, caption='サンプル画像')

# 【動画】
# video_file = open('movie.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

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

    # 【ラジオボタン】
    # 第一引数:ラベル、第二引数:選択肢のタプル
    gender = st.radio(
        '性別',
        ('男性', '女性', 'その他')
    )

    # 【複数選択】
    # 第一引数:ラベル、第二引数:選択肢のタプル
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '音楽', '映画鑑賞', '読書', '旅行'))

    # 【チェックボックス】
    # 第一引数:ラベル、第二引数:初期値
    mail_subscribe = st.checkbox('メールマガジンを購読する')

    # 【スライダー】
    # 第一引数:ラベル、第二引数:最小値、第三引数:最大値、第四引数:初期値
    height = st.slider('身長',min_value=100, max_value=200, value=100)

    # 【日付】
    start_date = st.date_input('開始日', datetime.date(2025, 10, 8))

    # 【カラー】
    color = st.color_picker('テーマカラー', '#00f900')

    # 【ボタン】
    # ボタンが押されたタイミングで値を受け取る
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    # print(f'submit_btn:{submit_btn}')
    # print(f'cancel_btn:{cancel_btn}')

    if submit_btn:
        st.text(f'ようこそ！{name}さん!\n{adress}に書類を送りました！')
        st.text(f'年齢層: {age_category}')
        st.text(f'性別: {gender}')
        st.text(f'趣味: {", ".join(hobby)}')
