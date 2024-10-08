import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime


st.title('Privacy Policy Training Site')

st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '２列目':[10,20,30,40]
# })

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
#st.write(df)

#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)

st.table(df.style.highlight_max(axis=0))#tableはstatic

"""
# 章
## 節
### 項

```python
import pandas as pd
```
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# 各問題と選択肢、正解を定義
questions = [
    "問題 1：プライバシーポリシーの目的は何ですか？",
    "問題 2：プライバシーポリシーにおける「個人情報」の定義として適切なものはどれですか？",
    "問題 3：個人情報の取得時に守るべきルールはどれですか？",
    "問題 4：個人情報を第三者に提供する場合に必要な手続きは？",
    "問題 5：個人情報の保管期間を超えたデータはどのように取り扱いますか？",
    "問題 6：個人情報の保護に関する「人的安全管理措置」とは何ですか？",
    "問題 7：個人情報の漏えいが発生した場合、最初に行うべき行動はどれですか？",
    "問題 8：個人情報の取り扱いに関する苦情や問い合わせがあった場合、どこに連絡するべきですか？",
    "問題 9：次のうち、「特定個人情報」に該当するものはどれですか？",
    "問題 10：個人情報保護の取り組みを見直すのはどのタイミングですか？"
]

options = [
    [
        "個人情報を適切に管理し、社内の業務効率を上げるため",
        "個人情報を保護し、法令やガイドラインを遵守するため",
        "個人情報を効率よく取得し、営業活動に活用するため"
    ],
    [
        "会社の全社員の連絡先情報",
        "特定の個人を識別できる情報で、氏名、生年月日などを含むもの",
        "企業名、住所、役職名などの法人情報"
    ],
    [
        "本人に通知せずに、目的に合った範囲内で取得する。",
        "法律で認められた適正な手段で、目的を明確にして取得する。",
        "業務効率を優先し、取得後に通知すればよい。"
    ],
    [
        "会社の代表者に許可を取る。",
        "社内会議で承認を得る。",
        "本人の同意を得る、または法律で認められた場合に限る。"
    ],
    [
        "保管期間を延長して引き続き保管する。",
        "データベースから削除し、紙資料はシュレッダーなどで廃棄する。",
        "特別な処理は行わず、他のデータと一緒に保管し続ける。"
    ],
    [
        "機密保持契約の締結や社員への教育訓練を行うこと。",
        "社内のすべてのパソコンにパスワードを設定すること。",
        "データのバックアップを定期的に取ること。"
    ],
    [
        "漏えいした情報を削除する。",
        "速やかに上司や個人情報管理者に報告する。",
        "関係者全員に謝罪する。"
    ],
    [
        "経理部門",
        "総務部門",
        "プライバシーポリシーで定められた「個人情報相談窓口」"
    ],
    [
        "個人の名前、住所、電話番号",
        "氏名と結びついたマイナンバー",
        "取引先担当者のメールアドレス"
    ],
    [
        "2年に一度",
        "事件事故が発生した時、および定期的に",
        "社内体制が変わった時のみ"
    ]
]

answers = [
    "個人情報を保護し、法令やガイドラインを遵守するため",
    "特定の個人を識別できる情報で、氏名、生年月日などを含むもの",
    "法律で認められた適正な手段で、目的を明確にして取得する。",
    "本人の同意を得る、または法律で認められた場合に限る。",
    "データベースから削除し、紙資料はシュレッダーなどで廃棄する。",
    "機密保持契約の締結や社員への教育訓練を行うこと。",
    "速やかに上司や個人情報管理者に報告する。",
    "プライバシーポリシーで定められた「個人情報相談窓口」",
    "氏名と結びついたマイナンバー",
    "事件事故が発生した時、および定期的に"
]


# 各質問に対するユーザーの回答を格納するリスト
user_answers = []

# 各質問に対して selectbox を表示し、ユーザーの回答を取得
for i, question in enumerate(questions):
    user_answer = st.selectbox(f"{question}", options[i], key=f"question_{i}")
    user_answers.append(user_answer)


# ユーザーの名前を入力させる
user_name = st.text_input("名前を入力してください:")

# 「回答を確定して結果を保存」ボタンを表示
if st.button("回答を確定して結果を保存"):
    # 名前が入力されているか確認
    if user_name:
        # 正解数をカウント
        correct_count = 0
        
        # 各回答をチェックし、正誤を判定
        for i, user_answer in enumerate(user_answers):
            if user_answer == answers[i]:
                correct_count += 1

        # 日付を取得
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 結果をCSV用のデータにまとめる
        data = {
            "Name": [user_name],
            "Scpre": [correct_count],
            "Date": [date]
        }
        df = pd.DataFrame(data)

        # CSVファイルとして保存
        file_name = f"{user_name}_test_result.csv"
        df.to_csv(file_name, index=False)

        # CSVファイルのダウンロードリンクを表示
        st.write("テストの結果が以下のファイルとして保存されました:")
        st.download_button(label="CSVをダウンロード", data=df.to_csv(index=False,encoding='utf-8-sig'), file_name=file_name, mime='text/csv')
        st.success(f"{user_name}さん、あなたの得点は {correct_count} / {len(questions)} です。")
    else:
        st.error("名前を入力してください。")

# 参考文献リンクを表示
st.markdown(
    """
    ### 参考文献
    プライバシーポリシーに関する法令やガイドラインについての詳細は、以下のリンクを参照してください。

    - [個人情報保護委員会（PPC） - 個人情報保護法について](https://www.ppc.go.jp/personalinfo/legal/)
    """
)

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# CSV ファイル名を指定
csv_file = "掲示板データ.csv"

# 1. CSV ファイルの存在を確認して、存在しない場合は新規作成
if not os.path.exists(csv_file):
    # 空のデータフレームを作成して初期化
    df = pd.DataFrame(columns=["名前", "内容", "日付"])
    # 空のデータフレームを CSV ファイルとして保存
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

# 2. 掲示板の投稿フォーム
st.title("簡易掲示板")

# 名前と投稿内容を入力
name = st.text_input("名前を入力してください:", key="name_input")
content = st.text_area("投稿内容を入力してください:", key="content_input")

# 投稿ボタンが押されたらデータを追加
if st.button("投稿", key="submit_button"):
    if name and content:
        # 日付を取得
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # CSV ファイルを読み込み
        df = pd.read_csv(csv_file, encoding='utf-8-sig')
        
        # 新しい行をデータフレーム形式で作成
        new_row = pd.DataFrame({"名前": [name], "内容": [content], "日付": [date]})
        
        # `pd.concat` を使用してデータフレームを結合
        df = pd.concat([df, new_row], ignore_index=True)
        
        # データフレームを CSV に保存
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        st.success("投稿が完了しました！ページを更新すると反映されます。")
    else:
        st.warning("名前と投稿内容を両方入力してください。")

# 3. 掲示板の内容を表示
st.header("掲示板の投稿一覧")

# 最新のデータを読み込んで表示
df = pd.read_csv(csv_file, encoding='utf-8-sig')
for i, row in df.iterrows():
    st.write(f"### {row['名前']} さん ({row['日付']})")
    st.write(row["内容"])
    st.write("---")

# 4. 投稿削除機能（管理用）
st.header("管理者用：投稿を削除する")
if st.checkbox("投稿を削除する", key="delete_checkbox"):
    # 削除したい行番号を選択
    index_to_delete = st.number_input("削除したい投稿の番号を入力（0から開始）", min_value=0, max_value=len(df)-1, step=1, key="index_input")
    if st.button("削除する", key="delete_button"):
        # 指定した行を削除して CSV に保存
        df = df.drop(index_to_delete).reset_index(drop=True)
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        st.success(f"投稿 {index_to_delete} を削除しました。")

