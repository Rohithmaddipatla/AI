from typing import List, Tuple
from collections import deque

State = Tuple[int, int, int, int, int, int]

def is_valid_state(state: State) -> bool:
    """
    Check if a state is valid according to the problem constraints.
    """
    m1, c1, b, m2, c2, _ = state

    # Non-negative counts
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False

    # Cannibals never outnumber missionaries where missionaries > 0
    if 0 < m1 < c1:
        return False
    if 0 < m2 < c2:
        return False

    return True


def get_successors(state: State) -> List[State]:
    """
    Generate all possible valid states that can be reached from a given state.
    """
    m1, c1, b, m2, c2, d = state
    successors: List[State] = []

    # Use *b* consistently as the boat position (1 = left, 0 = right)
    if b == 1:
        # boat is on the left side, move 1 or 2 people from left to right
        for i in range(3):          # missionaries moved
            for j in range(3):      # cannibals moved
                if 1 <= i + j <= 2:
                    new_state = (m1 - i, c1 - j, 0, m2 + i, c2 + j, 0)  # boat now on right
                    if is_valid_state(new_state):
                        successors.append(new_state)
    else:
        # boat is on the right side, move 1 or 2 people from right to left
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    new_state = (m1 + i, c1 + j, 1, m2 - i, c2 - j, 1)  # boat now on left
                    if is_valid_state(new_state):
                        successors.append(new_state)

    return successors


def breadth_first_search() -> List[State]:
    """
    Find the solution using a breadth-first search algorithm.
    """
    initial_state: State = (3, 3, 1, 0, 0, 1)  # boat on left
    goal_state:    State = (0, 0, 0, 3, 3, 0)  # boat on right

    visited = set([initial_state])
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        for successor in get_successors(state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [state]))
    return []
if __name__ == '__main__':
    solution = breadth_first_search()
    print("Solution:")
    for s in solution:
        print(s)