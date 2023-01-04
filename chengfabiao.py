row = 1


while row <= 9:
    col = 1
    while col <= row:
        mul = row * col
        print("%d * %d = %d" % (col, row, mul), end=" \t")
        col += 1

    print("")
    row += 1