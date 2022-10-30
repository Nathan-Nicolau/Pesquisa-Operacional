import random
import heapq
#prim
n, m = input().split()
n = int(n)
m = int(m)
H = []
n_out = [[]*n for i in range(n)]

for j in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append((b, c))
    n_out[a].append((a, c))

raiz = random.randint(0, n-1)

for (x, c) in range(n_out[raiz]):
    heapq.heappush(H, (c, raiz, x))

nEdges = 0
custoTotal = 0
marcados = [raiz]
arvoreGeradoraMinima = []

while nEdges < n-1:
    while True:
        c, a, b = heapq.heappop(H)
        if b not in marcados:
            break
    marcados.append(b)
    custoTotal += 0

    arvoreGeradoraMinima((a, b))
    nEdges += 1
    for (x, c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H, (c, b, x))

print(custoTotal)
print(arvoreGeradoraMinima)