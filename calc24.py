# calc24
n = [3, 7, 8, 9]
ops = ['add', 'sub', 'swap_sub', 'mul', 'div', 'swap_div']
rr = []

def calc(a, b, op):
    item = None
    if op == 'add':
        item = a + b
    elif op == 'sub':
        item = a - b        
    elif op == 'swap_sub':
        item = b - a
    elif op == 'mul':
        item = a * b
    elif op == 'div' and b != 0 and a % b == 0:
        item = int(a / b)
    elif op == 'swap_div' and a != 0 and b % a == 0:
        item = int(b / a)
    return item

def calc_result(r, i, j, a):
    for k in range(len(a)):
        if k != i and k != j:
            r.append(a[k])

def calc24(a, r, rr):
    result = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for op in ops:
                item = calc(a[i], a[j], op)
                if item != None:
                    result.append(item)
                    if len(r) == 0:
                        r.append((a[i], a[j], op))
                    else:
                        r.append((a[j], op))
                    calc_result(result, i, j, a)
                    if len(result) == 1:
                        if result[0] == 24:
                            if not r in rr:
                                rr.append(r[:])
                    else:
                        calc24(result[:], r, rr)

                    result = []
                    r.pop()         

calc24(n, [], rr)

def output(rr):
    for i in range(len(rr)):
        r = ''
        for j in range(len(rr[i])):
            item = rr[i][j]
            if j == 0:        
                if item[2] == 'add':
                    r = '(' + str(item[0]) + ' + ' + str(item[1]) + ')'
                elif item[2] == 'sub':
                    r = '(' + str(item[0]) + ' - ' + str(item[1]) + ')'
                elif item[2] == 'swap_sub':
                    r = '(' + str(item[1]) + ' - ' + str(item[0]) + ')'
                elif item[2] == 'mul':
                    r = str(item[0]) + ' * ' + str(item[1])
                elif item[2] == 'div':
                    r = str(item[0]) + ' / ' + str(item[1])
                elif item[2] == 'swap_div':
                    r = str(item[1]) + ' / ' + str(item[2])
            else:
                if item[1] == 'add':
                    r = '(' + r + ' + ' + str(item[0]) + ')'
                elif item[1] == 'sub':
                    r = '(' + r + ' - ' + str(item[0]) + ')'
                elif item[1] == 'swap_sub':
                    r = '(' + str(item[0]) + ' - ' + r + ')'
                elif item[1] == 'mul':
                    r = r + ' * ' + str(item[0])
                elif item[1] == 'div':
                    r = r + ' / ' + str(item[0])
                elif item[1] == 'swap_div':
                    r = str(item[0]) + ' / ' + r

        print(r)

output(rr)



