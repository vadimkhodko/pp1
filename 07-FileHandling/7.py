file = open("countries.txt", "r")
licznik = 1

for line in file:
    print(licznik, line, end="")
    licznik+=1

file.close()