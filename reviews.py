data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # for loop 把 f 清單裡的東西一個一個拿出來，存成line
		data.append(line) # 用.append()把line加入data清單
		# print(len(data)) # 每讀一行列印一次
		count += 1
		if count % 1000 == 0: # 把 count 和 1000 求餘數，如果餘數等於0:
			print(len(data))
print(len(data))
print(data[0]) #印出第一筆索引(index 0)
print('-----------')
print(data[1])