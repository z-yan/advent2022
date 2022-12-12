import string

letter_to_elevation = {
    letter: elevation for elevation, letter in enumerate(string.ascii_lowercase)
}
letter_to_elevation.update(
    {"S": letter_to_elevation["a"], "E": letter_to_elevation["z"]}
)

Vertex = tuple[int, int]
Graph = dict[Vertex, list[Vertex]]


def bfs_steps(start: Vertex, end: Vertex, graph: Graph) -> int:
    queue = [(start, 0)]
    visited = {start}

    while queue:
        curr_node, curr_steps = queue.pop(0)
        curr_steps += 1

        neighbors = graph[curr_node]

        if end in neighbors:
            return curr_steps

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, curr_steps))
                visited.add(neighbor)

    # end is unreachable from start
    return -1


if __name__ == "__main__":
    # Parse input as graph
    graph = dict()
    # Needed for part 2
    lowest_vertices = list()

    with open("input.txt") as f:
        input_data = f.read().splitlines()

    for row_number, row in enumerate(input_data):
        for col_number, letter in enumerate(row):
            curr_vertex = (row_number, col_number)

            if letter == "S":
                start = curr_vertex
            elif letter == "E":
                end = curr_vertex
            elif letter == "a":
                lowest_vertices.append(curr_vertex)

            curr_elevation = letter_to_elevation[letter]

            neighbors = [
                (row_number - 1, col_number),
                (row_number + 1, col_number),
                (row_number, col_number - 1),
                (row_number, col_number + 1),
            ]

            vertex_neighbors = list()

            for neighbor_row, neighbor_col in neighbors:
                if 0 <= neighbor_row < len(input_data) and 0 <= neighbor_col < len(row):
                    neighbor_elevation = letter_to_elevation[
                        input_data[neighbor_row][neighbor_col]
                    ]

                    neighbor_reachable = (
                        neighbor_elevation <= curr_elevation
                        or curr_elevation == neighbor_elevation - 1
                    )

                    if neighbor_reachable:
                        vertex_neighbors.append((neighbor_row, neighbor_col))

            graph[curr_vertex] = vertex_neighbors

    # Run BFS

    # Part 1
    steps = bfs_steps(start, end, graph)
    print(f"Steps to end: {steps}")

    # Part 2
    min_steps = min(
        steps
        for steps in (bfs_steps(start, end, graph) for start in lowest_vertices)
        if steps != -1
    )
    print(f"Minimum steps to end: {min_steps}")
