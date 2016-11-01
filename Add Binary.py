def addBinary(a, b):
    a_num = 0
    b_num = 0

    for i in a:
        a_num <<= 1
        a_num += int(i)

    for i in b:
        b_num <<= 1
        b_num += int(i)

    c = a_num + b_num
    result = []

    if c == 0:
        return "0"
    while (c):
        temp = c % 2
        result.insert(0,str(temp))
        c /= 2
    return "".join(result)

print(addBinary('11','1'))
