import streamlit as st

# タイトル
st.title("簡単な Streamlit アプリ")

# テキスト入力
name = st.text_input("名前を入力してください")

# ボタン
if st.button("送信"):
    st.write(f"こんにちは、{name} さん！")

# スライダー
age = st.slider("年齢", 0, 100, 25)
st.write(f"あなたの年齢は {age} 歳です。")

# チェックボックス
if st.checkbox("詳細を表示"):
    st.write("これは詳細情報です！")

# セレクトボックス
option = st.selectbox("好きな色を選んでください", ["赤", "青", "緑"])
st.write(f"あなたの好きな色は {option} ですね！")
