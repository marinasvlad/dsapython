def power(base, exponent):
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)

print(power(3,3))