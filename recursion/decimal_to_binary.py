import sys

sys.setrecursionlimit(10000)

def decimal_to_binary(n):
    assert n >= 0 and int(n) == n, "Trebuie sa introduci un intreg pozitiv"
    
    if n == 1:
        return 1
    else:
        return n % 2 + 10 * decimal_to_binary(int(n / 2))


n = int(sys.argv[1])
#n = 12
print(decimal_to_binary(n))

