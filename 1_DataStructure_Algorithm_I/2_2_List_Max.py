originData = [10, 5, 30, 40, 2, 4, 9, 80, 44, 23, 3]
copyData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 1way
def find_max1(data):
	max = data[0]
	for i in range(len(data)):
		if(max < data[i]):
			max = data[i]
	return max

# 2way
def find_max2(data):
	max = data[0]
	for val in data: # for의 in 뒤에 배열을 통째로 넣어도 된다
		if(max < val):
			max = val
	return max

print(find_max1(originData))