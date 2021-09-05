size = 5

a = [0 for i in range(size)]        # 每一行的皇后位于第几列
b = [0 for i in range(size)]        # 哪一列被皇后占据了
c = [0 for i in range(size * 2)]    # 哪个对角线被占据了 
d = [0 for i in range(size * 2)]    #

sum = 0

result = []

def Search(i):      # 当前考察第i行
    global a, b, c, d, size
    for j in range(0, size):
        if b[j] == 0 and c[i + j] == 0 and d[i - j + size] == 0:
            a[i] = j
            b[j] = 1
            c[i + j] = 1
            d[i - j + size] = 1
            if i == size - 1:
                Output()
            else:
                Search(i + 1)

            # 回溯点
            b[j] = 0
            c[i + j] = 0
            d[i - j + size] = 0

def Output():
    global sum
    sum += 1
    print("sum = ", sum)
    print(a)

Search(0)
