rows = 5

a = [0 for i in range(rows)]
b = [0 for i in range(rows)]
c = [0 for i in range(rows * 2)]
d = [0 for i in range(rows * 2)]

sum = 0

result = []

def Search(i):
    global a, b, c, d, rows
    for j in range(0, rows):
        if b[j] == 0 and c[i + j] == 0 and d[i - j + rows] == 0:
            a[i] = j
            b[j] = 1
            c[i + j] = 1
            d[i - j + rows] = 1
            if i == rows - 1:
                Output()
            else:
                Search(i + 1)

            b[j] = 0
            c[i + j] = 0
            d[i - j + rows] = 0

def Output():
    global sum
    sum += 1
    print("sum = ", sum)
    print(a)

Search(0)
