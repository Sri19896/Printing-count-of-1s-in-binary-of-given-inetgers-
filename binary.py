def binary(num):
    num = int(num)
    if num > 0:
        s = bin(num)
        s = str(s)
        return s.count('1')
    else:
        return('error')


print(binary(1234))
