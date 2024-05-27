N, M = map(int, input().split())

result = 0

for i in range(N):

    n = map(int, input().split())
    # 현재 행에서 가장 작은수
    min_value = min(n)
    # 가장 작은수 중에 큰 수
    result = max(result, min_value)

print(result)

