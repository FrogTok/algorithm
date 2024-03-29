# 1. x가 5로 나누어 떨어지면, 5로 나눈다.
# 2. x가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3. x가 2로 나누어 떨어지면, 2로 나눈다.
# 4. x에서 1을 뺀다.
# 위 네가지중 한가지 연산을 사용 가능하다.
# 특정 수를 1로 만들기위한 최소한의 연산 횟수를 구하라.

# 입력 예시
# 26
# 출력 예시
# 3

d = [0] * 30001

n = int(input())

for i in range(2, n + 1):
    if (d[i] == 0):
        d[i] = d[i - 1] + 1
        if (i % 5 == 0):
            d[i] = min (d[i], d[i // 5] + 1)
        if (i % 3 == 0):
            d[i] = min(d[i], d[i // 3] + 1)
        if (i % 2 == 0):
            d[i] = min(d[i], d[i // 2] + 1)

print(d[n])