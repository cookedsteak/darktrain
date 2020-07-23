# -*- coding: utf-8 -*-
import argparse
import xml.etree.ElementTree as et
import os

class_names = []
class_file_name = "classes.names"


def class_name_exists(name):
    if name not in class_names:
        class_names.append(name)
        return False
    return True


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    # 标注所在文件夹
    ap.add_argument("-x", "--annotations", required=True, help="origin annotations directory")
    args = vars(ap.parse_args())

    xml_list = os.listdir(args['annotations'])
    # 循环xml，将所有class放入字典
    for x in xml_list:
        in_file = open(args['annotations'] + '/' + x)
        tree = et.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls_n = obj.find('name').text
            class_name_exists(cls_n)

    # 将classes写入classes文件
    current_path = os.getcwd()
    out_file = open(current_path + '/' + class_file_name, 'w')
    for cls in class_names:
        out_file.write(cls + '\n')

