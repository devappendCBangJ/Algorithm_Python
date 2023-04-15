# 시간 복잡도 좋다

originData = list(map(int, input().split()))
destData = []

for i in range(len(originData)-1):
    min = originData[i]
    tmp = i
    for j in range(i+1, len(originData)):
        if(min > originData[j]):
            min = originData[j]
            tmp = j
    originData[tmp] = originData[i]
    originData[i] = min

for i in range(len(originData)):
    destData.append(originData[i])
print(destData)