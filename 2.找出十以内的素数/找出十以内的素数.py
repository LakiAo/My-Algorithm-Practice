sum = 0
for i in range(2,11):
    for q in range (2,11):
        if i % q != 0:
            sum += 1
            if sum == 8:
                print(i, "是素数")
    sum = 0