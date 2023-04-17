originData = [10, 5, 30, 40, 2, 4, 9, 80, 44, 23, 3]
copyData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(originData)

for i in range(len(originData)):
	copyData[i] = originData[i]

print(copyData)