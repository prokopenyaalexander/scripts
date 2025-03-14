import os
import sys
 
directory = ''


def build_tree(directory, prefix=""):

    items = os.listdir(directory)
    items.sort()

    for i in range(len(items)):
        item = items[i]
        path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        if is_last:
            branch = "└ "
        else:
            branch= "├── "
        print(prefix + branch + item)

        if os.path.isdir(path):
            if is_last:
                new_prefix = "    "
            else:
                new_prefix = "│   "
            build_tree(path, prefix + new_prefix)



def build_tree_(directory, prefix=""):
    items = os.listdir(directory)
    items.sort()
    folders = []
    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            folders.append(item)

    for i in range(len(folders)):
        folder = folders[i]
        path = os.path.join(directory, folder)
        is_last = i == len(folders) - 1
        
        if is_last:
            branch = "└─ "
        else:
            branch= "├── "
        print(prefix + branch + folder)

        if os.path.isdir(path):
            if is_last:
                new_prefix = "    "
            else:
                new_prefix = "│   "
                
            build_tree_(path, prefix + new_prefix)

    with open("tree.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        build_tree_(directory)


build_tree(directory)
build_tree_(directory)