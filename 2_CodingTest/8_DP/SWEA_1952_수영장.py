# input 불러오기
T = int(input())
for test_case in range(1, T + 1):
    # input 불러오기
    d, m, mmm, y = list(map(int, input().split()))
    plan = [0]
    plan.extend(list(map(int, input().split())))

    # dp_table 선언
    dp_table = [0] * 13

    for i in range(1, 12 + 1):
        # 월 이용권이 싼 경우
        if d * plan[i] >= m:
            dp_table[i] = dp_table[i-1] + m
        # 일 이용권이 싼 경우
        else:
            dp_table[i] = dp_table[i-1] + d * plan[i]
        # 3월 이상 부터 : 3달 연속 이용권이 싼 경우 추가
        if i > 2:
            if dp_table[i] >= dp_table[i-3] + mmm:
                dp_table[i] = dp_table[i-3] + mmm

    if dp_table[12] >= y:
        print(f'#{test_case} {y}')
    else:
        print(f'#{test_case} {dp_table[12]}')

# ---------------------------------------------------
# 다른 사람 : DP 풀이 -> if가 아니라 min 사용해도 되구나!
# https://codinghani.tistory.com/36
# ---------------------------------------------------
"""
T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    expense = [0 for _ in range(13)]

    for i in range(1, 13):
        # 하루, 한달 비교
        expense[i] = min(plan[i] * price[0], price[1]) + expense[i-1]
        # 3개월 이상부터 3달까지 비교
        if i > 2:
            expense[i] = min(expense[i], price[2] + expense[i-3])
    # 1년 비교
    ans = min(expense[12], price[3])
    print(f'#{tc} {ans}')
"""

# ---------------------------------------------------
# 다른 사람 : DP 풀이 -> 리스트를 생성해두고, 리스트 자체에 min을 하면 최소값인 원소가 나오구나!
# https://mungto.tistory.com/254
# ---------------------------------------------------
"""
T = int(input())
for t in range(1, T + 1):
    # 일, 1달, 3달, 1년 이용권
    price_list = list(map(int, input().split()))
    # 월별 이용날
    month_list = list(map(int, input().split()))
    # 결과 저장 변수 그 달의 최저값을 저장한다.
    result_list = [0] * 13
    for n in range(1, 13):
        # 가격을 저장할 임시변수
        a = [0, 0, 987654321, 987654321]
        # 일권으로 계산했을때, 전달비용 + 참여일수 * 일비
        a[0] = result_list[n - 1] + month_list[n - 1] * price_list[0]
        # 1달권으로 계산했을때, 전달비용 + 1달권 비용
        a[1] = result_list[n - 1] + price_list[1]
        # 3달권으로 계산했을때, 3달 전비용 + 3달권비용
        if n >= 3:   a[2] = result_list[n - 3] + price_list[2]
        # 1년권으로 계산했을때, 1년비용
        if n >= 12:   a[3] = price_list[3]
        # 현시점에서 제일 적은 비용의 값을 넣는다.
        result_list[n] = min(a)
    print('#{} {}'.format(t, result_list[12]))
"""

# ---------------------------------------------------
# 다른 사람 : DFS 풀이 -> DFS로 min_memory 지속적으로 update! 근데 이미 지나간 곳도 계속해서 탐색해서 연산량 많을듯
# https://developer-ellen.tistory.com/78
# ---------------------------------------------------
"""
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(m, cash):
    global min_money
    if m >= 13:
        min_money = min(min_money, cash)
        return
    else:
        print(m, cash)
        dfs(m+1, cash+money[0]*month[m])
        dfs(m+1, cash+money[1])
        dfs(m+3, cash+money[2])

for test_case in range(1, T+1):
    money = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    min_money = money[3]
    dfs(1, 0)

    print(f'#{test_case} {min_money}')
"""
