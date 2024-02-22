import sys

sys.setrecursionlimit(10000)

def power(base, exp):
    assert base >= 1 and exp >= 1 and int(base) == base and int(exp) >= 1, "Numerele trebuie sa fie numere intregi mai mari ca 0"
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)





base = int(sys.argv[1])
exp = int(sys.argv[2])

print(power(base, exp))

