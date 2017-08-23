numsTaken = [2, 5, 10]

print("here are the numbers that are still avail")

for n in range(1, 12):
    if n in numsTaken:
        continue
    print(n)
