import os
from pathlib import Path


class FileInstance:

    @classmethod
    def start(cls, target_path):
        return FileInstance(Path('/'), Path(target_path))

    def __repr__(self):
        return f"FileInstance({self.full_path})"

    def __str__(self):
        return f'{self.path} - {self.full_path}'

    def __init__(self, file, full_path):
        """
        :type file: Path
        :type full_path: Path
        """
        self.path = file
        if not isinstance(file, Path):
            self.path = Path(file)
        self.full_path = Path(full_path).resolve()
        if not self.path.is_absolute():
            self.full_path = self.full_path.resolve()
        self.file_name = self.full_path.name

        self.is_dir = self.full_path.is_dir()

        self.parent_dir = self.full_path.parent
        self.children = self.get_children() if self.is_dir else []
        self.file_extension = self.full_path.suffix
        # if not self.is_dir else None
        # self.file_size = os.path.getsize(file) if not self.is_dir else None

    def get_children(self):
        if self.is_dir:
            return [FileInstance(self.path / file.name, self.full_path / file) for file in self.full_path.iterdir()]
        return []

    def get_parent(self):
        return self.parent_dir


def main():
    file = FileInstance.start('C:/Users/carlj/Downloads')
    to_check = [file]

    while len(to_check) > 0:
        current = to_check.pop(0)
        children = current.get_children()
        for child in children:
            if child.is_dir:
                to_check.append(child)
            else:
                print(child)


if __name__ == "__main__":
    main()
