#streamlit streamlitrun a.py
import streamlit as st


支払金額 = st.number_input('支払金額を入力', min_value=0, max_value=1000, value=0)
源泉徴収税額 = st.number_input('源泉徴収税額を入力', min_value=0, max_value=1000, value=0)
社会保険料等の金額 = st.number_input('社会保険料等の金額を入力', min_value=0, max_value=1000, value=0)

手取り金額 = 支払金額 - 源泉徴収税額 - 社会保険料等の金額
st.write("あなたの手取り金額は", 手取り金額, "円です。")

## Github
# Github>Repositories>New
# Repository name入力, Public選択
# Create repository

## Terminal
# gitの初期化
# git init
# リポジトリを紐づける
# git remote add origin https://github.com/volbas/FP.git
# requirements.txt作成
# 外部ライブラリを入力
# 全てのファイル・ディレクトリを追加
# git add .
# ファイルをコミット
# git commit -m "1st commit"　
# ファイルの更新
# git push origin master
# *** Please tell me who you are.と聞かれたら
# git config --global user.email ここに自分のアドレス
# git config --global user.name ここに自分の名前

## Github
# リロード F5
# ファイルがアップロードされる

## Streamlit
# New app
# 作成したRepositoryを選択肢から選択
# プログラムを記載したpythonファイル名を入力
# Deploy!
# Webアプリ公開完了
# Your appsからURLをコピーして共有