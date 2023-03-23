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