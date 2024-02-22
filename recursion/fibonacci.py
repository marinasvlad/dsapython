import sys;

sys.setrecursionlimit(100000)

def fibonacci(n):
    assert n >= 0 and int(n) == n, "You must provide a positive integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(sys.argv[1])

print(fibonacci(n))