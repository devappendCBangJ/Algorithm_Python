data = ['A','B','C','D']

def insert_data(position, name):
	if position < 0 or position > len(data):
		print("out of range...")
		return

	data.append(None)
	kLen = len(data)
	for i in range(kLen-1, position,-1): # kLen-1 : 마지막 인덱스
		data[i] = data[i-1]
		data[i-1] = None
	data[position] = name

print(data)
insert_data(2, 'B2')
print(data)
insert_data(1, 'A2')
print(data)