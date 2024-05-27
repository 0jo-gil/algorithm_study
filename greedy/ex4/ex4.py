# 내 답안
N, K = map(int, input().split())
result = 0

#
# while True:
#     if N == 1:
#         break
#     elif N % K == 0:
#         N = N // K
#         result += 1
#     else:
#         N -= 1
#         result += 1
#
# print(result)

# 제공답안
# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1빼기
    while N & K != 0:
        N -= 1
        result += 1
    # N을 K로 나누기
    N //= K
    result += 1

while N > 1:
    N -= 1
    result += 1

print(result)


