# Q4
def sieve(m, n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(m, n + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    m = 10
    n = 20
    print("Prime numbers in range (", m, ", ", n, ") are:")
    sieve(m, n)
