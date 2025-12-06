from typing import List, Tuple, Set

State = Tuple[Tuple[int, int], Tuple[Tuple[int, ...], ...]]

def get_successors(state: State) -> List[State]:
    """
    Generate all possible valid states that can be reached from a given state.
    """
    position, grid = state
    successors: List[State] = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = position
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            # copy grid and possibly clean new cell
            new_grid = [list(row) for row in grid]
            if new_grid[new_x][new_y] == 1:
                new_grid[new_x][new_y] = 0
            # convert back to tuple-of-tuples for hashability
            successors.append(((new_x, new_y), tuple(tuple(r) for r in new_grid)))
    return successors

def depth_first_search(state: State, visited: Set[State]) -> bool:
    """
    Find the solution using a depth-first search algorithm.
    """
    # goal: all cells are 0
    if all(all(cell == 0 for cell in row) for row in state[1]):
        return True

    visited.add(state)

    for successor in get_successors(state):
        if successor not in visited:
            if depth_first_search(successor, visited):
                return True
    return False

if __name__ == '__main__':
    grid = [
        [0, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]

    initial_state: State = ((0, 0), tuple(tuple(r) for r in grid))

    if depth_first_search(initial_state, set()):
        print("The room can be cleaned.")
    else:
        print("The room cannot be cleaned.")