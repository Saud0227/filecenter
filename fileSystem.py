from fileInstance import FileInstance, FileObject, FolderObject


class FileSystem:
    def __init__(self, root_path):
        self.root_path = root_path

        self.root = FileInstance.start(root_path)

    def list_files(self):
        to_check = [self.root]
        out = []

        while len(to_check) > 0:
            current = to_check.pop(0)
            if isinstance(current, FileObject):
                out.append(current)
            else:
                to_check.extend(current.children)

        return out


def main():
    file_system = FileSystem('C:/Users/carlj/Downloads')
    # print(file_system.list_files())
    for i in file_system.root:
        print(i.file_name)

    print(file_system.root[2])
    print(file_system.root[3])
    print(file_system.root.object_size)


if __name__ == "__main__":
    main()
