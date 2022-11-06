def f(x):
    a=True
    for i in range(0,len(x)):
        if (x[i] != "0" and x[i] != "1"):
            a=False
    return a

print(f("111a12"))
