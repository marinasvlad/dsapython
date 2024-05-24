def fibbonaci(n):
    if n in [0, 1]:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)

print(fibbonaci(5))