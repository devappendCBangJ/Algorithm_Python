# # 순차 탐색
# list1 = [1, 2, 4, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 22, 26, 28, 29]
#
# print(list1)
# num = int(input('target number : '))
#
# for i in range(len(list1)):
#     if (list1[i] == num):
#         print(i)
#         break
        
# 이진 탐색
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2 # // : 몫만 취함
        if(target == data[mid]):
            return mid
        elif(target < data[mid]):
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

data = [1, 2, 4, 6, 7, 8, 10, 12, 17, 18, 19, 20, 22, 25, 26, 28]

num = binary_search(data, int(input('target_number : ')), 0, len(data))
print(num)