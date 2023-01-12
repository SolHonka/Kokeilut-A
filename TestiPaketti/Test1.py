def reduce_fraction(fraction):
    numer, denom = fraction
    for i in range(min(numer, denom), 0, -1):
        if numer % i == 0 and denom % i == 0:
            gcd = i
            break
    numer //= gcd
    denom //= gcd
    return (numer, denom)


print((21,108))


