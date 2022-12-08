def parse_input(file_path: str) -> list[list[int]]:
    return [
        [int(tree) for tree in line] for line in (open(file_path).read().splitlines())
    ]


def get_column(grid: list[list], col_index: int) -> list:
    return [el for row in grid for j, el in enumerate(row) if j == col_index]


def calculate_score(tree: int, other_trees: list[int]) -> int:
    return next(
        (i + 1 for i, other_tree in enumerate(other_trees) if other_tree >= tree),
        len(other_trees),
    )


if __name__ == "__main__":
    tree_grid = parse_input("input.txt")
    grid_size = len(tree_grid)
    edge_indices = (0, grid_size - 1)

    visible_count = 0
    max_scenic_score = 0

    for i, curr_row in enumerate(tree_grid):
        for j, tree in enumerate(curr_row):
            # Edge trees
            if i in edge_indices or j in edge_indices:
                visible_count += 1
            else:
                # Inner trees

                # Part 1
                curr_column = get_column(tree_grid, j)

                max_left = max(curr_row[:j])
                max_right = max(curr_row[j + 1 :])

                max_up = max(curr_column[:i])
                max_down = max(curr_column[i + 1 :])

                visible_count += int(
                    tree > max_left
                    or tree > max_right
                    or tree > max_up
                    or tree > max_down
                )

                # Part 2
                up_score = calculate_score(tree, curr_column[:i][::-1])

                left_score = calculate_score(tree, curr_row[:j][::-1])

                down_score = calculate_score(tree, curr_column[i + 1 :])

                right_score = calculate_score(tree, curr_row[j + 1 :])

                scenic_score = left_score * right_score * up_score * down_score

                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

    print(f"Visible trees: {visible_count}")
    print(f"Highest scenic score: {max_scenic_score}")
