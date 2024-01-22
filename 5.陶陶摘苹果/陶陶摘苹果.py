apple = input().split(' ')
height = int(input())
get = 0
for i in range(10):
    if int(apple[i]) <= height+30:
        get += 1
print(get)