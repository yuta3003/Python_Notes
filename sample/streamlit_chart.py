import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# タイトル
st.title("Streamlitによるデータ可視化サンプル")

# ダミーデータを作成
np.random.seed(42)
df = pd.DataFrame({
    "日付": pd.date_range(start="2024-03-01", periods=10, freq="D"),
    "売上": np.random.randint(100, 500, size=10),
    "顧客数": np.random.randint(20, 100, size=10),
    "カテゴリ": np.random.choice(["A", "B", "C"], size=10)
})

# 折れ線グラフ（売上の推移）
st.subheader("📈 売上推移（折れ線グラフ）")
st.line_chart(df.set_index("日付")["売上"])

# 棒グラフ（カテゴリ別売上）
st.subheader("📊 カテゴリ別売上（棒グラフ）")
category_sales = df.groupby("カテゴリ")["売上"].sum()
st.bar_chart(category_sales)

# 円グラフ（カテゴリごとの売上割合）
st.subheader("📎 カテゴリ別売上割合（円グラフ）")
fig, ax = plt.subplots()
ax.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90)
ax.axis("equal")  # 円を真円にする
st.pyplot(fig)

# データ表示
st.subheader("📋 データ一覧")
st.dataframe(df)
