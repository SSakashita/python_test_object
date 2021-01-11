"""
このファイルに解答コードを書いてください
"""

FILE_NAME = 'input.txt'

with open(FILE_NAME, mode='rt', encoding='utf-8') as f:
	d = {}
	for line in f:
		# 整数と文字列を辞書に格納
		line = line.replace('\n', '')
		if ':' in line:
			i, s = line.split(':')
			d[str(i)] = s
		# 数字のみの場合は入力値として格納
		else:
			input_num = int(line)

	# 辞書を昇順に並び替え
	d = sorted(d.items(), key=lambda x:x[0])

	# 出力の作成
	answer_text = ''
	for i, s in d: #もし入力値の約数であれば出力テキストの後ろに追加
		if input_num % int(i) == 0:
			answer_text += s

	# 回答の出力
	if answer_text == '': # もしテキストが空白であれば入力値を返す
		print(input_num)
	else: #テキストがあればそれを返す
		print(answer_text)





