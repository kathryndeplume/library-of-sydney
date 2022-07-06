#!/usr/bin/env python3

def generate(a):
    n = len(a)
    c = [0] * n
    p = 1

    print(a)

    i = 0
    while i < n:
        if c[i] < i:
            if (i % 2) == 0:
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]

            print(a)
            p += 1

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    print(p)

if __name__ == "__main__":
    generate(list(range(0, 8)))
