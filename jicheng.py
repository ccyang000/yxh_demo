def jicheng(num):
    if num == 1:
        return 1
    temp = jicheng(num - 1)
    return num * temp

result = jicheng(5)
print(result)