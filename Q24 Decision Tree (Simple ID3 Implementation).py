import math

data = [
    ["Sunny", "Hot",    "No"],
    ["Sunny", "Mild",   "No"],
    ["Overcast", "Hot", "Yes"],
    ["Rain", "Mild",    "Yes"],
    ["Rain", "Cool",    "Yes"]
]

def entropy(rows):
    total = len(rows)
    yes = sum(1 for r in rows if r[-1]=="Yes")
    no  = total - yes
    if yes==0 or no==0: return 0
    p1=yes/total; p2=no/total
    return -(p1*math.log2(p1) + p2*math.log2(p2))

def split(rows, col, val):
    return [r for r in rows if r[col]==val]

def best_attr(rows):
    base = entropy(rows)
    best_gain = -1
    best_col = None
    for c in range(len(rows[0]) - 1):
        vals = set(r[c] for r in rows)
        gain = base - sum((len(split(rows,c,v))/len(rows))*entropy(split(rows,c,v)) for v in vals)
        if gain > best_gain:
            best_gain = gain
            best_col = c
    return best_col

def build(rows):
    if entropy(rows)==0:
        return rows[0][-1]
    col = best_attr(rows)
    tree = {col:{}}
    vals = set(r[col] for r in rows)
    for v in vals:
        tree[col][v] = build(split(rows,col,v))
    return tree

print(build(data))
