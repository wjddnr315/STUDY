import sys
i = sys.stdin.readline

n, m = map(int, i().split())

pokemons1 = {str(t + 1): i().rstrip() for t in range(n)}
pokemons2 = {v: k for k, v in pokemons1.items()}
for _ in range(m):
    k = i().rstrip()
    try:
        print(pokemons1[k])
    except KeyError:
        print(pokemons2[k])
