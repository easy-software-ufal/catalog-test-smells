# This is an auxiliary tool to identify all the files on the repo.

import glob
import os

if __name__ == '__main__':
    folder_names = []
    for root, dirs, files in os.walk('Test Smells', topdown=False):
        for name in dirs:
            folder_names.append(os.path.join(root, name))
    # def smells_loader_closure_all():
    list = glob.glob("**", recursive=True)
    file = open('dirs.txt',mode='x')
    for item in list:
        if item in folder_names:
            list.remove(item)
            continue
        if 'venv' in item or 'tools' in item or '.py' in item or '.pyc' in item or '__pycache__' in item or '.txt' in item or '.md' in item or '.csv' in item or '\\' not in item:
            continue
        file.write(item)
        file.write('\n')
