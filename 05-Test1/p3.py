def f(x):
    counter = 0

    if(x >= 5):
        counter =counter + x//5
        x = x%5

    if(x >= 2):
        counter = counter + x//2
        x = x%2

    if (x >= 1):
        counter = counter + x//1
        x = x %1

    return(counter)

print(f(27))