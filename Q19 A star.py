from heapq import heappush, heappop

g = {
    'A':{'B':1,'C':4},
    'B':{'D':2,'E':5},
    'C':{'F':3},
    'D':{}, 'E':{}, 'F':{}
}

h = {'A':7,'B':6,'C':5,'D':0,'E':0,'F':0}

o = []
heappush(o,(h['A'],0,'A',[]))
v = set()

while o:
    f,gc,n,path = heappop(o)
    if n in v: continue
    v.add(n)
    if h[n] == 0:
        print(path+[n])
        break
    for x,c in g[n].items():
        heappush(o,(gc+c+h[x],gc+c,x,path+[n]))
