# 하노이탑 시각화 : https://www.youtube.com/watch?v=FYCGV6F1NuY

N = int(input())

def hanoi(_num, _from, _to, _other):
    if _num == 0:
        return
    hanoi(_num-1, _from, _other, _to)
    print(_from, '->', _to)
    hanoi(_num-1, _other, _to, _from)

print(2**N - 1, "회 움직임")
hanoi(N, 1, 3, 2)