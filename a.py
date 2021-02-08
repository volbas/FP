#streamlit run a.py
import streamlit as st



支払金額 = st.number_input('支払金額を入力', min_value=0, max_value=1000, value=0)
源泉徴収税額 = st.number_input('源泉徴収税額を入力', min_value=0, max_value=1000, value=0)
社会保険料等の金額 = st.number_input('社会保険料等の金額を入力', min_value=0, max_value=1000, value=0)

手取り金額 = 支払金額 - 源泉徴収税額 - 社会保険料等の金額
st.write("あなたの手取り金額は", 手取り金額, "円です。")
