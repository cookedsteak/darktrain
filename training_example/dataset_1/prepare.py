# -*- coding: utf-8 -*-
import os
import shutil

import xml.etree.ElementTree as ET

current_path = os.getcwd()
classes_name = "classes.names"
backup_name = "backup"

# pre-check
# check the dataset directories that required
if not os.path.exists(current_path + '/Annotations') or not os.path.exists(current_path + '/JPEGImages') or not os.path.exists(current_path + '/JPEGImages_val'):
    raise SystemExit("Missing Annotations or JPEGImages, aborting...")


print("Pre-check finished, now making directories...")

if not os.path.exists(os.getcwd() + '/' + backup_name):
    os.mkdir(os.getcwd() + '/' + backup_name)

if not os.path.exists(os.getcwd() + '/labels/'):
    os.mkdir(os.getcwd() + '/labels/')

print("Finished making directories, now making txt files...")

# generate train_name  train_path txt
jpg_path = current_path + "/JPEGImages/"
jpg_val_path = current_path + "/JPEGImages_val/"
fileList = os.listdir(jpg_path)
fileList_val = os.listdir(jpg_val_path)
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
new_file_val_name = open(val_file_name, 'a')
new_file_val_path = open(val_file_path, 'a')

link_str = '.'
for i in fileList:
    fn = fileList[n].split(".")
    fn.pop(-1)
    img_name = link_str.join(fn)

    img_path = jpg_path + fileList[n]

    new_file_name.write(img_name)
    new_file_name.write("\n")

    new_file_path.write(img_path)
    new_file_path.write("\n")

    n += 1

n = 0
for i in fileList_val:
    fn = fileList_val[n].split(".")
    fn.pop(-1)
    img_name = link_str.join(fn)

    img_path = jpg_val_path + fileList_val[n]

    new_file_val_name.write(img_name)
    new_file_val_name.write("\n")

    new_file_val_path.write(img_path)
    new_file_val_path.write("\n")

    n += 1

new_file_name.close()
new_file_path.close()
new_file_val_name.close()
new_file_val_path.close()

# shutil.copy(train_file_name, val_file_name)
# shutil.copy(train_file_path, val_file_path)

print("Finished making txt files, now dealing with labels...")

# set classes.names
# fill classes.names with the classes you need
f = open('classes.names', 'r')
line = f.read()
classes = line.split('\n')

while '' in classes:
    classes.remove('')


print("Labels finished, making data file...")

f_data = open("my.data", "w")
f_data.write("classes=" + str(len(classes)) + "\n")
f_data.write("train=" + current_path + "/" + train_file_path + "\n")
f_data.write("valid=" + current_path + "/" + val_file_path + "\n")
f_data.write("names=" + current_path + "/" + classes_name + "\n")
f_data.write("backup=" + current_path + "/" + backup_name)

f_data.close()

print("Start converting...")

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
    # xml path
    in_file = open(current_path + '/Annotations/%s.xml' % image_id, encoding='utf-8')
    # txt file path
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
    # train images path
    list_file_train.write(current_path + '/JPEGImages/%s.jpg\n' % image_id)
    convert_annotation(image_id)

list_file_train.close()

for image_id in image_ids_val:
    # validation images path
    list_file_val.write(current_path + '/JPEGImages_val/%s.jpg\n' % image_id)
    convert_annotation(image_id)

list_file_val.close()

print ('All finished!')