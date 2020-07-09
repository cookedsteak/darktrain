# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET

'''
    ##################################
    Stage1 Prepare raw files
    ##################################
'''
# directory names
# please run this script inside your data-set directory
current_path = os.getcwd()
classes_name = "classes.names"
backup_name = "backup"
an_name = 'Annotations'
tr_name = 'JPEGImages'
# val_name = 'JPEGImages'  # val_name = 'JPEGImages_val'

# pre-check
# check the data-set directories that required
if not os.path.exists(current_path + '/' + an_name) or \
        not os.path.exists(current_path + '/' + tr_name):
    raise SystemExit("Missing Annotations or JPEGImages, aborting...")

print("Pre-check finished, now making directories...")

if not os.path.exists(os.getcwd() + '/' + backup_name):
    print("Creating backup...")
    os.mkdir(os.getcwd() + '/' + backup_name)

if not os.path.exists(os.getcwd() + '/labels/'):
    print("Creating labels...")
    os.mkdir(os.getcwd() + '/labels/')

print("Finished making directories, now making txt files...")

# generate train_name  train_path txt
jpg_path = current_path + "/" + tr_name + "/"
fileList = os.listdir(jpg_path)
n = 0
# 之后生成label的依据
train_file_name = "train_name.txt"
train_file_path = "train_path.txt"

if os.path.exists(train_file_name):
    os.remove(train_file_name)

if os.path.exists(train_file_path):
    os.remove(train_file_path)

new_file_name = open(train_file_name, 'a')
new_file_path = open(train_file_path, 'a')

link_str = '.'
for i in fileList:
    fn = fileList[n].split(".")
    fn.pop(-1)

    img_name = link_str.join(fn).strip()
    new_file_name.write(str(img_name, encoding="utf-8"))
    new_file_name.write("\n")

    img_path = jpg_path + fileList[n]
    img_path.encode('utf-8').strip()
    new_file_path.write(img_path)
    new_file_path.write("\n")

    n += 1

new_file_name.close()
new_file_path.close()

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
f_data.write("valid=" + current_path + "/" + train_file_path + "\n")
f_data.write("names=" + current_path + "/" + classes_name + "\n")
f_data.write("backup=" + current_path + "/" + backup_name)

f_data.close()

print("Start converting...")

'''
    ##################################
    Stage2 Convert xml labels
    ##################################
'''


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(iid):
    # xml path
    in_file = open(current_path + '/' + an_name + '/%s.xml' % image_id, encoding='utf-8')
    # txt file path
    out_file = open(current_path + '/labels/%s.txt' % iid, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xml_box = obj.find('bndbox')
        b = (float(xml_box.find('xmin').text), float(xml_box.find('xmax').text), float(xml_box.find('ymin').text),
             float(xml_box.find('ymax').text))
        print("converting" + iid)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


image_ids_train = open(current_path + '/' + train_file_name).read().strip().split()
# image_ids_val = open(current_path + '/' + val_file_name).read().strip().split()
list_file_train = open(current_path + '/' + train_file_path, 'w')
# list_file_val = open(current_path + '/' + val_file_path, 'w')

for image_id in image_ids_train:
    # train images path
    list_file_train.write(current_path + '/%s/%s.jpg\n' % (tr_name, image_id))
    convert_annotation(image_id)

list_file_train.close()

print ('All finished!')
