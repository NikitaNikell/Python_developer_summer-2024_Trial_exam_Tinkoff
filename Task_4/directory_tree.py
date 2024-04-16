def directory_tree(paths):
    tree = {}
    for path in paths:
        directories = path.split('/')[:]
        current = tree
        for directory in directories:
            if directory not in current:
                current[directory] = {}
            current = current[directory]
    return tree


def print_directory_tree(tree, indent=0):
    for directory, subtree in sorted(tree.items()):
        print(' ' * indent + directory)
        if subtree:
            print_directory_tree(subtree, indent + 2)  # Увеличиваем отступ для вложенных директорий


n = int(input())  # Количество директорий

paths = [input() for _ in range(n)]  # Абсолютные пути ко всем директориям

directory_tree = directory_tree(paths)
print_directory_tree(directory_tree)
