def alpha_beta(node,depth,alpha,beta,maxp,tree):
    if depth==0 or node not in tree:
        return tree.get(node,0)
    if maxp:
        v=-999
        for c in tree[node]:
            v=max(v,alpha_beta(c,depth-1,alpha,beta,False,tree))
            alpha=max(alpha,v)
            if alpha>=beta: break
        return v
    else:
        v=999
        for c in tree[node]:
            v=min(v,alpha_beta(c,depth-1,alpha,beta,True,tree))
            beta=min(beta,v)
            if beta<=alpha: break
        return v

tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':3,'E':5,'F':2,'G':9
}

print(alpha_beta('A',2,-999,999,True,tree))
