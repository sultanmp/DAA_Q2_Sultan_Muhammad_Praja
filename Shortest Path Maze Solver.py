from collections import deque

# Directions: Up, Right, Down, Left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] 

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # return reversed path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if (0 <= next_row < rows and 0 <= next_col < cols and 
                maze[next_row][next_col] == 0 and
                (next_row, next_col) not in visited):

                queue.append((next_row, next_col))
                visited.add((next_row, next_col))
                parent[(next_row, next_col)] = current  # save the parent

    return None  # if no path is found

# Test
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

print(bfs(maze, start, end))
