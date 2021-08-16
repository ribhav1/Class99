import os
import shutil


# BACKS UP FILES IN FOLDER

# path = 'C:/Users/risha/Downloads/new_directory'
#
# print('before copying: ')
# print(os.listdir(path))
#
# source = 'C:/Users/risha/Downloads/new_directory/directory/test1.txt'
# destination = 'C:/Users/risha/Downloads/new_directory/'
#
# copy = shutil.copy(source, destination)
#
# print('after copying: ')
# print(os.listdir(path))


# SORTS FILES BY EXTENSION INTO FOLDERS

path = input('Enter directory for files to be sorted: ')

directory_list = os.listdir(path)

for file in directory_list:
    name, ext = os.path.splitext(file)

    ext = ext[1:]

    if ext == '':
        continue
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)