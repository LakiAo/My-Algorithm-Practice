#很好 洛谷不给我过 原因是用了数组 太暴力了
pet = [[-1 for _ in range(1000)] for i in range(1000)]

n = int(input())
for _ in range(n):
    _input = input().split(' ')
    a = int(_input[0])
    b = int(_input[1])
    g = int(_input[2])
    k = int(_input[3])
    for a in range(a,g+a):
        for b in range(b,k+b):
            pet[a][b] = _+1
_input2 = input().split(' ')
print(pet[int(_input2[0])][int(_input2[1])])