def linearFibo(k):
	if k > 1: # [1, 1] -> [1+1, 1] -> [2+1, 2] -> [3+2, 3] -> [5+3, 5] -> [13, 8] -> ...
		data = linearFibo(k-1)
		temp = data[0]
		data[0] = data[1]
		data[1] = temp + data[1]
		return data
	else:
		return [1, 1]

for i in range(10, 400, 1):
	print(i, 'fibo = ', linearFibo(i)[0])
