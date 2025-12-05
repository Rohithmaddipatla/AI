def safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True
n = int(input("Enter number of queens (e.g., 8): "))
board = [-1] * n
def solve(row):
    if row == n:
        return True
    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            if solve(row + 1):
                return True
    return False
if solve(0):
    for r in range(n):
        for c in range(n):
            if board[r] == c:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")