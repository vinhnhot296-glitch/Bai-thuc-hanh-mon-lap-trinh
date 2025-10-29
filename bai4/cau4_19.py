def sieve_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu
P = tuple(sieve_primes(10**6))

print("Số lượng số nguyên tố nhỏ hơn 1 triệu:", len(P))
print("10 số nguyên tố đầu tiên:", P[:10])
print("10 số nguyên tố cuối cùng:", P[-10:])
