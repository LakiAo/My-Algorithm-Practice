#果然还得动动脑子 不能只靠暴力算法
n = int(input())
pet = []
for _ in range(n):
    _input = input().split(' ')
    a = int(_input[0])
    b = int(_input[1])
    g = int(_input[2])
    k = int(_input[3])
    pet.append([a,a+g,b,b+k])
_search = input().split(' ')
x = int(_search[0])
y = int(_search[1])
for _ in range(n-1,-1,-1):
    if pet[_][0] <= x <= pet[_][1] and pet[_][2] <= y <= pet[_][3]:
        print(_+1)
        break
    elif _ == 0:
        print("-1")