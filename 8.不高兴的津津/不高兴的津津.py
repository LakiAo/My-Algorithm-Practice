motion = 0
mark = 8
for i in range(1,8):
    hour = input().split(' ')
    if(int(hour[0])+int(hour[1]) > mark):
        motion = i
        mark = int(hour[0])+int(hour[1])
print(motion)