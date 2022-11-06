def f(x):
    if (len(x) != 16):
        return "incorrect number"
    else:
        list1 = list(x)
        for i in range(2,12):
            list1[i] = "*"
        x = ''.join(list1)
        return x

     
print(f("1111000011110000"))