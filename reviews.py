#留言分析程式
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # for loop 把 f 清單裡的東西一個一個拿出來，存成 line 字串
		data.append(line) # 用.append()把line加入data清單
		# print(len(data)) # 每讀一行列印一次
		count += 1
		if count % 1000 == 0: # 把 count 和 1000 求餘數，如果餘數等於0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data: #把 data 清單裡的字串一個一個拿出來，存成 d 字串
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# good = []
# for d in data:
#	if 'good' in d: # 檢查 good 字串是否有在 d 字串裡面
#		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])

# 清單快寫法list comprehension，等於line 26 - 29
# good = [d for d in data if 'good' in d]
# print(good) # 確認結果

good = [1 for d in data if 'good' in d]
print(good)

bad = ['bad' in d for d in data]
print(bad)

# line 40-41 的原本寫法
# bad = []
# for d in data:
# 	bad.append('bad' in d)

#文字計數功能

wc = {} # word_count
word_count = 0
for d in data:
	words = d.split() # 拿掉' '之後，split會預設為空白做切割
	for word in words:
		if word in wc:
			# 自己練習 word_count += 1
			wc[word] += 1
		else:
			# 自己練習 wc[word] = word_count
			wc[word] = 1 # 新增key進wc字典，value = 1

for word in wc: # for loop來印字典
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))  # 印出字典的長度

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本功能')
