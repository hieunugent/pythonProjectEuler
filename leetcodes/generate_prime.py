def generate_prime(n):
    primes=[]
    is_prime = [False, False] + [True]*(n-1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2, n+1, p):
                is_prime[i] = False
    return primes

print(generate_prime(10))



