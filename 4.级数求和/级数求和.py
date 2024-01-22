#暴力算法 不适用于k=1的情况 建议对k=1单独写一个if
k = int(input())
sum = 0
n = 1
while sum < k:
    sum = sum + 1/n
    n += 1
print(n-1)