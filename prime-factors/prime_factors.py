#zzzZZzZZZ math
def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d #hllo opratr r u dere wut r u
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac