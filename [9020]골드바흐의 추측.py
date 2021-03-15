from itertools import combinations


def get_primes(n):
    numbers = [True] * n
    numbers[0] = numbers[1] = False
    for i in range(n):
        if numbers[i]:
            for j in range(i*2, n, i):
                numbers[j] = False
    return [num for num, prime in enumerate(numbers) if prime]


primes = get_primes(5082)
partitions = list(combinations(primes, 2))+list((x, x) for x in primes)
dic = {}
for i in partitions:
    if sum(i) not in dic:
        dic[sum(i)] = []
    dic[sum(i)].append(i)
for key in dic.keys():
    dic[key] = sorted(dic[key], key=lambda x: -x[0])[0]
for _ in range(int(input())):
    n = int(input())
    print(f"{dic[n][0]} {dic[n][1]}")
