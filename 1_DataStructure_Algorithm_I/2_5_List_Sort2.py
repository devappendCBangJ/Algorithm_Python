# 시간복잡도 좋지 않다

inData = [10, 5, 30, 40, 2, 4, 9]
outData = [0, 0, 0, 0, 0, 0, 0]

pre_bound = 0
for i in range(0, len(inData)):
    low_bound = 100
    for j in range(0, len(inData)):
        if inData[j] > pre_bound:
            if inData[j] < low_bound:
                low_bound = inData[j]

    outData[i] = low_bound
    pre_bound = low_bound

print(outData)