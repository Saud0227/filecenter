# import os
from pathlib import Path


class FileInstance:

    @classmethod
    def start(cls, target_path):
        return FileInstance(Path('/'), Path(target_path))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_path})"

    def __str__(self):
        return f'{self.path} - {self.object_size}'

    def __new__(cls, file, full_path, parent=None):
        if cls is FileInstance:
            # print("!")
            cls = FolderObject if full_path.is_dir() else FileObject
        return super().__new__(cls)


    def __init__(self, file, full_path, parent=None):
        """
        :type file: Path
        :type full_path: Path
        :type parent: FileInstance
        """
        # This is a base class and should not be instantiated
        # This code should only be run by subclass

        self.path = file
        if not isinstance(file, Path):
            self.path = Path(file)

        self.full_path = Path(full_path).resolve()

        if not self.path.is_absolute():
            self.full_path = self.full_path.resolve()

        self.file_name = self.full_path.name

        self.parent_dir = parent
        self.path_to_root = [self]

        self.object_size = 0

        current_object = self
        while current_object.parent_dir is not None:
            current_object = current_object.parent_dir
            self.path_to_root.insert(0, current_object)

    def get_parent(self):
        return self.parent_dir

    def _get_size(self):
        # This method should be overridden by subclasses
        return 0


class FileObject(FileInstance):
    def __init__(self, file, full_path, parent=None):
        super().__init__(file, full_path, parent)
        self.object_size = self._get_size()
        self.file_extension = self.full_path.suffix

    def _get_size(self):
        return self.full_path.stat().st_size


class FolderObject(FileInstance):

    def __iter__(self):
        return self.children.__iter__()

    def __init__(self, file, full_path, parent=None):
        super().__init__(file, full_path, parent)
        self.children = self.get_children()
        self.object_size = self._get_size()

    def __getitem__(self, item):
        return self.children[item]

    def __len__(self):
        return len(self.children)

    def _get_size(self):
        return sum([child._get_size() for child in self.children])

    def get_children(self):
        return [FileInstance(self.path / file.name, self.full_path / file, self)
                for file in self.full_path.iterdir()]


def main():
    file = FileInstance.start(Path('C:/Users/CarlJ/Downloads'))
    to_check = [file]
    last = None

    # print('\\' + '\\'.join([i.file_name for i in last.path_to_root]))
    # print(type(last))
    # print(last.get_size())
    # print(type(last.parent_dir))
    # print(last.parent_dir.get_size())
    print(file.get_size())


if __name__ == "__main__":
    main()
