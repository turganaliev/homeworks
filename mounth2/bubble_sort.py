l = [9, 5, 6, 1, 4, 6]

for i in range(len(l) - 1):
    n = 0
    for d in range(len(l) - 1):
        if l[n] > l[n + 1]:
            a = l[n]
            b = l[n + 1]
            l[n] = b
            l[n + 1] = a
        n += 1

print(l)