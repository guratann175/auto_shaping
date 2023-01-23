'''
文章を自動で整形するツールを作る!!
'''
import pyperclip

text = pyperclip.paste()

# replace: 改行の削除 \rと\nの二つが存在する
text = text.replace("\n", "")
text = text.replace("\r", "")

# ピリオドで文章を分離する
text = text.split('.')

for i in range(len(text)):
    # 各テキストにピリオドと改行文字を付ける
    re_text = text[i] + '.' + '\n\n'
    text[i] = re_text
    # print(text[i])

# 配列を文字列に変換
comp_text = "".join(text)
# print(comp_text)

# クリップボードにコピーする
pyperclip.copy(comp_text)
