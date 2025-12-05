from collections import deque
goal = "123456780"
def moves(s):
    i = s.index("0")
    step = []
    pos = [i-3, i+3, i-1, i+1]
    for p in pos:
        if 0 <= p < 9:
            if i % 3 == 0 and p == i - 1:
                continue
            if i % 3 == 2 and p == i + 1:
                continue
            lst = list(s)
            lst[i], lst[p] = lst[p], lst[i]
            step.append("".join(lst))
    return step
start = input("Start state: ")
q = deque([start])
vis = {start: None}
while q:
    s = q.popleft()
    if s == goal:
        break
    for m in moves(s):
        if m not in vis:
            vis[m] = s
            q.append(m)
if goal not in vis:
    print("This puzzle has no solution.")
    exit()
path = []
t = goal
while t:
    path.append(t)
    t = vis[t]
path.reverse()
for p in path:
    print(p[:3])
    print(p[3:6])
    print(p[6:])
    print()