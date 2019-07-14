import os
import shutil

path = os.getcwd() + "/" + "JPEGImages/"

fileList = os.listdir(path)

# print(fileList)

n = 0

train_file_name = "train_name.txt"
train_file_path = "train_path.txt"
val_file_name = "val_name.txt"
val_file_path = "val_path.txt"


if os.path.exists(train_file_name):
    os.remove(train_file_name)

if os.path.exists(train_file_path):
    os.remove(train_file_path)

if os.path.exists(val_file_name):
    os.remove(val_file_name)

if os.path.exists(val_file_path):
    os.remove(val_file_path)

new_file_name = open(train_file_name, 'a')
new_file_path = open(train_file_path, 'a')

for i in fileList:
    fn = fileList[n].split(".", 1)
    img_name = fn[0]

    img_path = path + fileList[n]

    new_file_name.write(img_name)
    new_file_name.write("\n")

    new_file_path.write(img_path)
    new_file_path.write("\n")

    n += 1

new_file_name.close()
new_file_path.close()

shutil.copy(train_file_name, val_file_name)
shutil.copy(train_file_path, val_file_path)

print("finished")