# while loops.py

# perulangan while
i = 1
while i <= 5:
    print("Perulangan ke-", i)
    i += 1

# break
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)