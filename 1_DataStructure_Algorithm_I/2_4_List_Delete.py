data = ['A','B','C','D']

def insert_data(position, name):
	if position < 0 or position > len(data):
		print("out of range...")
		return

	data.append(None)
	kLen = len(data)
	for i in range(kLen-1, position,-1):
		data[i] = data[i-1]
		data[i-1] = None
	data[position] = name

def delete_data(position):
    if position < 0 or position > len(data):
        print("out of range...")
        return

    kLen = len(data)
    data[position] = None
    for i in range(position+1, kLen): # kLen-1 : 마지막 인덱스
	    data[i-1] = data[i]
	    data[i] = None
    del data[kLen-1]

print(data)
delete_data(2)
print(data)
delete_data(1)
print(data)