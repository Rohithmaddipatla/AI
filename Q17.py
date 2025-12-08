g = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[], 'E':[], 'F':[]
}

s = ['A']
v = set()

while s:
    n = s.pop()
    if n in v: continue
    v.add(n)
    print(n)
    for x in g[n]:
        s.append(x)
