from typing import List, Optional, Dict, Callable
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class FileSystemObject:
    def __init__(self, name: str):
        self.name = name

    def get_size(self) -> int:
        raise NotImplementedError()


class File(FileSystemObject):
    def __init__(self, name: str, size: int):
        super(File, self).__init__(name)
        self.size = size

    def __str__(self):
        return f'{self.name}  (file, size={self.size})'

    def get_size(self) -> int:
        return self.size


class Directory(FileSystemObject):
    def __init__(self, name: str, parent: Optional['Directory'] = None):
        super(Directory, self).__init__(name)
        self.parent: Optional[Directory] = parent
        self.children: List[FileSystemObject] = []

    def __str__(self):
        return f'{self.name}  (dir)'

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)


def get_sum_of_directory_sizes(terminal_output: List[str], maximum_size: int) -> int:
    root: Optional[Directory] = build_file_system(terminal_output)

    logger.debug('')
    visualize_file_system(root)
    directory_sizes: List[int] = []
    find_folders_below_size_limit(root, maximum_size, directory_sizes)
    return sum(directory_sizes)


def get_smallest_directory_size_to_delete(terminal_output: List[str], maximum_size: int) -> int:
    root: Optional[Directory] = build_file_system(terminal_output)
    if not root:
        return 0

    total_disk_size = 70000000
    disk_in_use = root.get_size()
    free_space = total_disk_size - disk_in_use
    size_to_be_deleted = maximum_size - free_space
    logger.debug('')
    logger.debug(f'Free space: {free_space}, we need {maximum_size}, so we need to delete {size_to_be_deleted}')

    logger.debug('')
    visualize_file_system(root)
    directory_sizes: List[int] = []
    find_folders_above_size_limit(root, size_to_be_deleted, directory_sizes)
    return min(directory_sizes)


def build_file_system(terminal_output: List[str]) -> Optional[Directory]:
    root: Optional[Directory] = None
    current_directory: Optional[Directory] = None

    for terminal_item in terminal_output:
        if terminal_item.startswith('$'):
            # command to be executed
            command_parts = terminal_item.split(' ')
            command = command_parts[1]

            command_function = FUNCTIONS[command]
            if len(command_parts) == 3:
                current_directory = command_function(current_directory, command_parts[2])
                if root is None:
                    root = current_directory
            else:
                current_directory = command_function(current_directory)

        else:
            # output of a command
            if terminal_item.startswith('dir'):
                # skip
                continue
            else:
                file_size_string, file_name = terminal_item.split(' ')
                file_size: int = int(file_size_string)
                file = File(file_name, file_size)
                if current_directory is None:
                    raise ValueError('No current directory')

                current_directory.children.append(file)

    return root


def visualize_file_system(file_system_object: Optional[FileSystemObject], indent: int = 0):
    if logger.level != logging.DEBUG:
        return

    if file_system_object is None:
        return

    logger.debug(f'{" " * indent}- {file_system_object}')
    if isinstance(file_system_object, Directory):
        for child in sorted(file_system_object.children, key=lambda x: x.name):
            visualize_file_system(child, indent + 2)


def find_folders_below_size_limit(file_system_object: Optional[FileSystemObject],
                                  maximum_size: int, sizes_below_limit: List[int]) -> None:
    if file_system_object is None:
        return

    directory_size = file_system_object.get_size()
    if isinstance(file_system_object, Directory):
        if directory_size <= maximum_size:
            sizes_below_limit.append(directory_size)
        for child in file_system_object.children:
            find_folders_below_size_limit(child, maximum_size, sizes_below_limit)


def find_folders_above_size_limit(file_system_object: FileSystemObject,
                                  minimum_size: int, sizes_above_limit: List[int]) -> None:
    directory_size = file_system_object.get_size()
    if isinstance(file_system_object, Directory):
        if directory_size >= minimum_size:
            sizes_above_limit.append(directory_size)
        for child in file_system_object.children:
            find_folders_above_size_limit(child, minimum_size, sizes_above_limit)


def execute_cd(current_directory: Directory, folder_name: str):
    if current_directory is None:
        return Directory(folder_name)
    else:
        if folder_name == '..':
            return current_directory.parent
        else:
            new_directory = Directory(folder_name, current_directory)
            current_directory.children.append(new_directory)
            return new_directory


def execute_ls(current_directory: FileSystemObject):
    return current_directory


FUNCTIONS: Dict[str, Callable[..., Optional[Directory]]] = {
    'cd': execute_cd,
    'ls': execute_ls
}
