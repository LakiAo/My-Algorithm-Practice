a = input().split(' ')
n = int(a[0])
k = int(a[1])
sum = n
sum = sum + int(n/k)
while int(n/k)+n%k > k:
        sum += int((int(n/k)+n%k)/k)
print(sum)
#上述代码是迷迷糊糊写出来的 不知道为什么有两个检测点时间太长过不了

b = input().split(' ')
y = int(a[0])
jl = int(a[1])
yt = 0
num = 0
while y != 0:
    y -= 1
    num += 1
    yt += 1
    if(yt = jl):
          yt -= jl
          num += 1
print(num)