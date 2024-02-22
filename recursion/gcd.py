import sys

sys.setrecursionlimit(10000)

def gcd(a,b):
    assert int(a) == a and int(b) == b, "Trebuie sa introduci numere intregi!"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a%b)


a = int(sys.argv[1])
b = int(sys.argv[2])

print(gcd(a,b))