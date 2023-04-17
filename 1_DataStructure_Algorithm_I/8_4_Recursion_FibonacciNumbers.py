def binaryFib(k):
	if k > 1:
		return binaryFib(k - 1) + binaryFib(k-2)
	else:
		return 1

for i in range(10, 400, 1):
	print(i, 'fibo = ', binaryFib(i))
