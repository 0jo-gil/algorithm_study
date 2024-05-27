# 내 답안
# a = [5, 8, 3]
# b = [2, 4, 5, 4, 6]
#
# N = a[0]
# M = a[1]
# K = a[2]
#
# count = 0
#
# c = sorted(b, reverse=True)
#
#
# for i in range(M):
#     tmp = i % K
#
#     if i == 0:
#         count += c[0]
#         continue
#
#     if tmp > 0:
#         count += c[0]
#     else:
#         count += c[1]
#
# print(count)

# 서적상 답안

# n m k 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
result = 0
data.sort()

first = data[n - 1]
second = data[n - 2]

while True:
    for i in range(k):
        if m == 0:
            break

        result += first
        m -= 1
    if m == 0:
        break

    result += second
    m -= 1

print(result)





