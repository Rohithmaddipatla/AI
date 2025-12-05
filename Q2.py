A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8, 9],
    [1, 2, 3]
]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print("Resultant Matrix:")
for r in result:
    print(r)