def union(a, b):
    a = list(a)
    b = list(b)
    c = b.copy()
    for i in range(len(a)):
        if a[i] not in c:
            c.append(a[i])
    return c

