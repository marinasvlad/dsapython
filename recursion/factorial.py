import sys;

sys.setrecursionlimit(10000)

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'; 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(sys.argv[1])

print(factorial(n))