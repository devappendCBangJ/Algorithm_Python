# https://yangnyang.tistory.com/14

def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    elif n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [j for j in arr]
            ans.remove(arr[i]) # 선택했던 원소를 다시 선택하지 않기 위해
            for p in perm(ans, n-1):
                result.append([arr[i]] + p)

    return result

arr = [1, 2 ,3]
print(perm(arr, 1))
print(perm(arr, 2))
print(perm(arr, 3))