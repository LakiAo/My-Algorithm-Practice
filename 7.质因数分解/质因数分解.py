n = int(input())
zhishu = []
for i in range(2,n):
    if(n % i == 0):
        zhishu.append(i)
        if(len(zhishu)==1):
            break
print(int(n/zhishu[0]))
#一开始出现了超时的问题，一直从1到n都除一遍来找到最大的质数，后来发现只需要取最小的质数再用n除以这个质数对应的就是最大的那个质数了