'''
翻訳用の文章を自動で整形するツールを作る!!
'''
import pyperclip

# コピーされた文章を取り出す
text = pyperclip.paste()

# replace: 改行の削除 \rと\nの二つが存在する
text = text.replace("\n", "")
text = text.replace("\r", "")

# ピリオドで文章を分離する listになる
text = text.split('.')

re_text = []
for i in range(len(text)):
    # splitによりピリオドが消えているので、付けなおす
    text[i] += '.'
    # 文字数が10文字未満なら、前の文章に結合する
    if len(text[i]) < 10:
        print(text[i])
        re_text[len(re_text)-1] = "".join([re_text[len(re_text)-1], text[i]])
    else:
        re_text.append(text[i])

for i in range(len(re_text)):
    # 各テキストに改行文字を付ける
    re_text[i] += '\n\n'
    # print(text[i])

# 配列を文字列に変換
comp_text = "".join(re_text)
# print(comp_text)

# クリップボードにコピーする
pyperclip.copy(comp_text)
