colors = ["R","G","B"]
regions = {"A":["B","C"],"B":["A","C"],"C":["A","B"]}
assign = {}

def ok(r,c):
    for n in regions[r]:
        if n in assign and assign[n]==c:
            return False
    return True

def solve(rlist):
    if not rlist: return True
    r = rlist[0]
    for c in colors:
        if ok(r,c):
            assign[r]=c
            if solve(rlist[1:]): return True
            del assign[r]
    return False

solve(list(regions.keys()))
print(assign)
