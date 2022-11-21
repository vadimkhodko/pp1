films = ("Jocker","Fight club", "American psycho", "Cars", "King lion")

with open("films.txt", "w") as f:
    for film in films:
        f.write(film)
        f.write('\n')