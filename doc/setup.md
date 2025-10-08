# Windows 環境での Streamlit 環境構築

## 1. Python のインストール確認

まず、Python がインストールされているか確認します。コマンドプロンプトまたは PowerShell を開いて:

```bash
python --version
```

Python 3.8 以上が必要です。インストールされていない場合は、[Python 公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールしてください。

### ※ただし、3.14 は新しいバージョンのため多くのパッケージがまだ対応していないため、エラーになる可能性があるので、3.11 または 3.12 を使用することを推奨します。(2025/10/08 現在)

## 2. 仮想環境の作成（推奨）

プロジェクト用のフォルダを作成し、仮想環境を作ります:

```bash
# 【プロジェクトフォルダの作成】
mkdir streamlit_project
cd streamlit_project

# 【仮想環境の作成】
#python -m venv [仮想環境名]
python -m venv stremalit_venv

# 【仮想環境の有効化】
#[仮想環境名]\Scripts\activate
streamlit_venv\Scripts\activate

# 【有効化されたかの確認】
# 以下のようにパスの前に[仮想環境名]が表示されれば有効化されている
(streamlit_venv) ~/
```

## 3. Streamlit のインストール

仮想環境内で Streamlit をインストール:

pip(Python パッケージ管理システム)を使用して streamlit をインストールします。

```bash
pip install streamlit
```

### Steramlit の依存パッケージである`pyarrow`のビルドに失敗した場合の解決方法

**解決方法 1:　ビルド済みの`pyarrow`を使用(推奨)**

pip と setuptools を最新版にアップグレードしてから、再度インストールをする

```bash
# 【pipのアップグレード】
python -m pip install --upgrade pip

# 【バージョン確認】
pip list

# 【再度Streamlitをインストール】
pip install streamlit
```

**解決方法 2:　 pyarrow を先に個別インストール**

pyarrow のビルド済みバイナリを直接インストール

```bash
# pyarrowを先にインストール
pip install pyarrow

# その後Streamlitをインストール
pip install streamlit
```

## 4. インストールの確認

正しくインストールされたか確認:

```bash
streamlit --version
```

## 5. 最初のアプリを作成

`app.py` というファイルを作成し、以下のコードを記述:

```python
import streamlit as st

st.title("初めてのStreamlitアプリ")
st.write("こんにちは、Streamlit!")

name = st.text_input("お名前を入力してください")
if name:
    st.write(f"ようこそ、{name}さん!")
```

## 6. アプリの実行

以下のコマンドで実行:

```bash
streamlit run app.py
```

自動的にブラウザが開き、アプリが表示されます（通常は `http://localhost:8501`）。

## トラブルシューティング

- **コマンドが認識されない場合**: Python のパスが通っているか確認してください
- **ポートが使用中の場合**: `streamlit run app.py --server.port 8502` で別のポートを指定できます

##　 7.ライブラリのインストール

### Pillow のインストール

画像処理ライブラリの Pillow をインストールします。

このライブラリを使用して、Streamlit で作成したページに画像を表示させます。

```bash
# Pillowのインストール
pip install Pillow

# バージョンの確認
pip show Pillow
```

これで環境構築は完了です!公式ドキュメント（https://docs.streamlit.io/）も非常に充実しているので、併せて参照することをお勧めします。
