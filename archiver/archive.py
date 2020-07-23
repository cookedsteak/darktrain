# -*- coding: utf-8 -*-
import argparse
import os, shutil
import random
import string
import re
import time


def make_dir_if_not_exists(my_path):
    if not os.path.exists(my_path):
        print("Creating folder..." + my_path)
        os.mkdir(my_path)
    return my_path


def make_random_str():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


def make_new_filename():
    return str(int(time.time())) + '_' + make_random_str()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    # 图片所在文件夹
    ap.add_argument("-j", "--images", required=True, help="origin images directory")
    # 标注所在文件夹
    ap.add_argument("-x", "--annotations", required=True, help="origin annotations directory")
    # 移动到的目标文件夹
    ap.add_argument("-d", "--des", default="final-popo", help="new destination directory")
    args = vars(ap.parse_args())

    jpeg_folder_name = "JPEGImages"
    xml_folder_name = "Annotations"
    current_path = os.getcwd()
    # 查看目标文件夹下的子文件夹是否齐全
    make_dir_if_not_exists(current_path + '/' + args['des'])
    d_jpg_path = make_dir_if_not_exists(current_path + '/' + args['des'] + '/' + jpeg_folder_name)
    d_xml_path = make_dir_if_not_exists(current_path + '/' + args['des'] + '/' + xml_folder_name)

    # 图片文件夹下的文件名列表
    jpg_list = os.listdir(args['images'])
    # 以图片为主要依据，开始轮询
    for j in jpg_list:
        # 过滤隐藏文件
        if re.match('^\.', j) is not None:
            continue
        # 过滤文件夹
        if os.path.isdir(args['images'] + '/' + j):
            continue
        pn = j.split(".")
        # 检查文件类型是否正确
        if len(pn) < 2:
            continue
        if pn[1] != "jpg" and pn[1] != "jpeg":
            continue
        # 获取文件名（除去后缀）
        jpg_ext = pn.pop(-1)
        # 对应xml文件名
        xml_file_name = pn[0] + ".xml"
        # 是否存在对应的xml文件
        if os.path.exists(args['annotations'] + '/' + xml_file_name):
            # 移动jpg和xml到新文件夹
            try:
                new_name = make_new_filename()
                shutil.move(args['images'] + '/' + j,
                            d_jpg_path + '/' + new_name + '.' + jpg_ext)
                shutil.move(args['annotations'] + '/' + xml_file_name,
                            d_xml_path + '/' + new_name + '.xml')
            except BaseException or Exception as e:
                raise e
