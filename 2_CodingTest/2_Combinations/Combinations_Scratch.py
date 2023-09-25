# https://yangnyang.tistory.com/14

def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1): # i가 len(arr) - n + 1보다 커지면 n개보다 적은 수를 선택하는 것이 되어버리므로, 범위 지정
            for c in comb(arr[i + 1:], n - 1): # 현재 원소보다 인덱스가 낮은 원소 or 선택했던 원소를 다시 선택하지 않기 위해
                result.append([arr[i]] + c)

    return result

arr = [1, 2, 3]
print(comb(arr, 1))
print(comb(arr, 2))
print(comb(arr, 3))