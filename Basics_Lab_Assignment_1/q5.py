# Q5
def gcd(a, b):
    if b == 0:
        return a
    if a == 1 or b == 1:
        return 1
    if a <= b:
        return gcd(a, b % a)
    return gcd(b, a % b)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


x = int(input())
y = int(input())
print("GCD is: ", gcd(x, y))
print("LCM is: ", lcm(x, y))
