def union(a, b):
    a = list(a)
    b = list(b)
    c = b.copy()
    for j in a:
        q = False
        for i in b:
            if j == i:
                q = True
        if q == False:
            c.append(j)

    if len(c) <= 1:
        return c
    else:
        for iter_num in range(len(c) - 1, 0, -1):
            for idx in range(iter_num):
                if c[idx] > c[idx + 1]:
                    temp = c[idx]
                    c[idx] = c[idx + 1]
                    c[idx + 1] = temp

    return c

def crossing(a, b):
    a = list(a)
    b = list(b)
    c = []
    for j in a:
        for i in b:
            if j == i:
                c.append(j)

    if len(c) <= 1:
        return c
    else:
        for iter_num in range(len(c) - 1, 0, -1):
            for idx in range(iter_num):
                if c[idx] > c[idx + 1]:
                    temp = c[idx]
                    c[idx] = c[idx + 1]
                    c[idx + 1] = temp
    return c


def diff(a, b):
    a = list(a)
    b = list(b)
    c = a.copy()
    for j in a:
        q = False
        for i in b:
            if j == i:
                q = True
        if q == True:
            c.remove(j)

    if len(c) <= 1:
        return c
    else:
        for iter_num in range(len(c) - 1, 0, -1):
            for idx in range(iter_num):
                if c[idx] > c[idx + 1]:
                    temp = c[idx]
                    c[idx] = c[idx + 1]
                    c[idx + 1] = temp
    return c

def symetricdiff(a, b):
    a = list(a)
    b = list(b)
    c = []
    for j in range(len(a)):
        if a[j] not in b:
            c.append(a[j])
    for i in range(len(b)):
        if b[i] not in a:
            c.append(b[i])

    if len(c) <= 1:
        return c
    else:
        for iter_num in range(len(c) - 1, 0, -1):
            for idx in range(iter_num):
                if c[idx] > c[idx + 1]:
                    temp = c[idx]
                    c[idx] = c[idx + 1]
                    c[idx + 1] = temp
    return c

print(diff({1,2,3,9}, {2,9}))