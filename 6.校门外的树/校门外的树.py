ll = input().split(' ')
num = int(ll[0])
count = int(ll[1])
tree = [0] * (num+1)
sum = 0
for i in range(num+1):
    tree[i]=1
while count > 0:
    cut = input().split(' ')
    for i in range(int(cut[0]),int(cut[1])+1):
        tree[i]=0
    count -= 1
for i in range(num+1):
    if(tree[i] == 1):
        sum += 1
print(sum)