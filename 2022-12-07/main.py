from typing import Union


class Node:
    def __init__(self, parent: "Directory", name: str):
        self.parent = parent
        self.name = name
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value


class File(Node):
    def __init__(self, parent: "Directory", name: str, size: int):
        super().__init__(parent, name)
        self.size = size


class Directory(Node):
    def __init__(self, parent: Union["Directory", None], name: str):
        super().__init__(parent, name)
        self.children: list[Node] = list()

    @property
    def size(self):
        return sum(child.size for child in self.children)

    @size.setter
    def size(self, value):
        raise IsADirectoryError()

    @property
    def path(self):
        if self.parent:
            if self.parent.path == "/":
                separator = ""
            else:
                separator = "/"

            return self.parent.path + separator + self.name
        else:
            return self.name

    def get_child(self, name: str):
        for child in self.children:
            if child.name == name:
                return child

        return None


def parse_input(input_path: str) -> Directory:
    with open(input_path) as f:
        input_lines = f.read().splitlines()

    root_dir = Directory(name="/", parent=None)
    curr_dir = root_dir

    for line in input_lines:
        if line == "$ cd /":
            curr_dir = root_dir
        elif line == "$ cd ..":
            curr_dir = curr_dir.parent
        elif line.startswith("$ cd "):
            curr_dir = curr_dir.get_child(line[5:])
        elif line.startswith("dir "):
            curr_dir.children.append(Directory(parent=curr_dir, name=line[4:]))
        elif line == "$ ls":
            continue
        else:
            file_size, file_name = line.split()
            curr_dir.children.append(
                File(parent=curr_dir, name=file_name, size=int(file_size))
            )

    return root_dir


def get_dir_sizes(root_dir: Directory) -> dict[str, int]:
    result: dict[str, int] = {root_dir.path: root_dir.size}

    for child in root_dir.children:
        if isinstance(child, Directory):
            result.update(get_dir_sizes(child))

    return result


if __name__ == "__main__":
    root_dir = parse_input("input.txt")

    dir_sizes = get_dir_sizes(root_dir)

    # Part 1
    print(sum(size for size in dir_sizes.values() if size <= 100000))

    # Part 2
    print(
        min(
            size
            for size in dir_sizes.values()
            if size >= dir_sizes[root_dir.path] - 40000000
        )
    )
