from fileInstance import FileInstance


class FileSystem:
    def __init__(self, root_path):
        self.root_path = root_path

        self.root = FileInstance.start(root_path)

    def list_files(self):
        to_check = [self.root]
        out = []

        while len(to_check) > 0:
            current = to_check.pop(0)
            children = current.get_children()
            for child in children:
                if child.is_dir:
                    to_check.append(child)
                else:
                    out.append(child)
        return out


def main():
    file_system = FileSystem('C:/Users/carlj/Downloads')
    print(file_system.list_files())


if __name__ == "__main__":
    main()
