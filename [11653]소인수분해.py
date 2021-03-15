n = int(input())
while n != 1:
    is_prime = True
    for i in range(2, n // 2 + 1):
        if not n % i:
            n //= i
            break
