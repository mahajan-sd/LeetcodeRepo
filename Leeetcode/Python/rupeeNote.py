notes = [500, 200, 100, 50, 20, 10]

amount = 1530
temp = 0

i = 0
while amount > 0:
    notesCOunt = amount // notes[i]
    temp += notesCOunt
    amount = int(amount % notes[i])
    i += 1

print(temp)