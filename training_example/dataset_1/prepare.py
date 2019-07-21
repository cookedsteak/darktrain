import os
import shutil

import xml.etree.ElementTree as ET

current_path = os.getcwd()

# pre-check
# check the dataset directories that required
if not os.path.exists(current_path + '/Annotations') or not os.path.exists(current_path + '/JPEGImages'):
    raise SystemExit("Missing Annotations or JPEGImages, aborting...")


print("Making directories...")

if not os.path.exists(os.getcwd() + '/backup/'):
    os.mkdir(os.getcwd() + '/backup/')

if not os.path.exists(os.getcwd() + '/labels/'):
    os.mkdir(os.getcwd() + '/labels/')

print("Making txt files...")

# 根据JPEG中的文件，生成对应的 train_name  train_path txt
jpg_path = current_path + "/JPEGImages/"
fileList = os.listdir(jpg_path)
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

    img_path = jpg_path + fileList[n]

    new_file_name.write(img_name)
    new_file_name.write("\n")

    new_file_path.write(img_path)
    new_file_path.write("\n")

    n += 1

new_file_name.close()
new_file_path.close()

shutil.copy(train_file_name, val_file_name)
shutil.copy(train_file_path, val_file_path)

print("Finished making txt files, now dealing with labels....")

# 设置 classes.names 并输入你想要训练的类
# fill classes.names with the classes you need
f = open('classes.names', 'r')
line = f.read()
classes = line.split('\n')

while '' in classes:
    classes.remove('')


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return x,y,w,h


def convert_annotation(image_id):
    #这里改为xml文件夹的路径
    in_file = open(current_path + '/Annotations/%s.xml' % image_id)
    #这里是生成每张图片对应的txt文件的路径
    out_file = open(current_path + '/labels/%s.txt' % image_id, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes :
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


image_ids_train = open(current_path + '/' + train_file_name).read().strip().split()
image_ids_val = open(current_path + '/' + val_file_name).read().strip().split()
list_file_train = open(current_path + '/' + train_file_path, 'w')
list_file_val = open(current_path + '/' + val_file_path, 'w')

for image_id in image_ids_train:
    #这里改为样本图片所在文件夹的路径
    list_file_train.write(current_path + '/JPEGImages/%s.jpg\n' % image_id)
    convert_annotation(image_id)

list_file_train.close()

for image_id in image_ids_val:
    #这里改为样本图片所在文件夹的路径
    list_file_val.write(current_path + '/JPEGImages/%s.jpg\n' % image_id)
    convert_annotation(image_id)

list_file_val.close()

print ('All finished!')