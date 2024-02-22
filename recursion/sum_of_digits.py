import sys;

sys.setrecursionlimit(10000)

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "You must provide a positive integer"
    
    if n == 0:
        return n
    
    else:
        return n % 10 + sum_of_digits(int(n / 10))

n = int(sys.argv[1])

print(sum_of_digits(n))