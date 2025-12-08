from itertools import permutations

g = {
    0:{1:10,2:15,3:20},
    1:{0:10,2:35,3:25},
    2:{0:15,1:35,3:30},
    3:{0:20,1:25,2:30}
}

cities = [0,1,2,3]
best = 10**9

for p in permutations(cities[1:]):
    path = (0,)+p+(0,)
    cost = sum(g[path[i]][path[i+1]] for i in range(len(path)-1))
    best = min(best, cost)

print(best)
