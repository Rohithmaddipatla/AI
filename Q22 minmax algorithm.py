def minimax(node, depth, maxp, tree):
    if depth == 0 or node not in tree:
        return tree.get(node, 0)

    if maxp:
        best = -999
        for c in tree[node]:
            best = max(best, minimax(c, depth - 1, False, tree))
        return best
    else:
        best = 999
        for c in tree[node]:
            best = min(best, minimax(c, depth - 1, True, tree))
        return best

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3, 'E': 5, 'F': 2, 'G': 9
}

print(minimax('A', 2, True, tree))
