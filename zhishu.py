data = int(input("输入截止数值： "))

i = 0
l = 0
while i <= data:
    j = 1
    k = 0
    while j <= i:

        if i % j == 0:
            k += 1
        j += 1

    if k == 2:
        print(i)
        l += 1

    i += 1

print("0- %d 中一共有%d个质数" % (data, l))
