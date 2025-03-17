import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# -------------------------------
# データの準備
# -------------------------------
np.random.seed(42)
data = {
    "日付": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "売上": np.random.randint(100, 1000, size=30),
    "顧客数": np.random.randint(10, 100, size=30),
    "カテゴリ": np.random.choice(["A", "B", "C"], size=30)
}
df = pd.DataFrame(data)

# 日付型を datetime に変換
df["日付"] = pd.to_datetime(df["日付"])

# -------------------------------
# サイドバー (フィルタ機能)
# -------------------------------
st.sidebar.header("🔍 フィルタ")

# Streamlitでサポートされる日付型に変換
min_date = df["日付"].min().date()  # datetime.date に変換
max_date = df["日付"].max().date()  # datetime.date に変換

# 日付スライダー（datetime.date 型を使用）
selected_date_range = st.sidebar.slider(
    "表示する日付範囲",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# 選択した日付範囲に基づいてデータをフィルタリング
filtered_df = df[(df["日付"].dt.date >= selected_date_range[0]) & (df["日付"].dt.date <= selected_date_range[1])]

# カテゴリ選択フィルタ
selected_category = st.sidebar.selectbox("カテゴリを選択", ["すべて"] + list(df["カテゴリ"].unique()))
if selected_category != "すべて":
    filtered_df = filtered_df[filtered_df["カテゴリ"] == selected_category]

# -------------------------------
# メイン画面
# -------------------------------
st.title("📊 売上ダッシュボード")

# 💰 売上の概要
st.subheader("💰 売上の概要")
total_sales = filtered_df["売上"].sum()
average_sales = filtered_df["売上"].mean()
total_customers = filtered_df["顧客数"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("総売上", f"¥{total_sales:,}")
col2.metric("平均売上", f"¥{average_sales:.2f}")
col3.metric("顧客数", f"{total_customers:,} 人")

# 📈 売上推移（折れ線グラフ）
st.subheader("📈 売上推移")
st.line_chart(filtered_df.set_index("日付")["売上"])

# 📊 カテゴリ別売上（棒グラフ）
st.subheader("📊 カテゴリ別売上")
category_sales = filtered_df.groupby("カテゴリ")["売上"].sum()
st.bar_chart(category_sales)

# 🥧 売上の割合（円グラフ）
st.subheader("🥧 カテゴリ別売上割合")
fig, ax = plt.subplots()
ax.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90)
ax.axis("equal")
st.pyplot(fig)

# 📋 データ一覧
st.subheader("📋 データ一覧")
st.dataframe(filtered_df)

# -------------------------------
# まとめ
# -------------------------------
st.markdown("📝 **データはランダム生成されています**。日付やカテゴリを選択して、フィルタリング結果を確認できます！")
