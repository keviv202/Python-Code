def toHex(num):
    ret = ''
    letter = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    v=0
    if num == 0: return '0'
    if num < 0: num += 2 ** 32

    while num != 0:
        v = num & 15
        ret = letter[num & 15] + ret
        num >>= 4
    return ret

print(toHex(-2))