# -*- coding: utf-8 -*-
import argparse
import xml.etree.ElementTree as et
import os
from string import Template

class_names = []
class_file_name = "classes.names"


def make_dir_if_not_exists(my_path):
    if not os.path.exists(my_path):
        print("Creating folder..." + my_path)
        os.mkdir(my_path)
    return my_path


def class_name_exists(name):
    if name not in class_names:
        class_names.append(name)
        return False
    return True


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    # 标注所在文件夹
    ap.add_argument("-x", "--annotations", required=True, help="origin annotations directory")
    ap.add_argument("-d", "--des", default="final-pop", help="new destination directory")
    ap.add_argument("-c", "--cfg", default="./cfg_template/yolov3_cfg.tpl", help="path of template config file")
    args = vars(ap.parse_args())

    path_annotations = args['annotations'].rstrip('/')
    xml_list = os.listdir(path_annotations)
    current_path = os.getcwd()
    make_dir_if_not_exists(current_path + '/' + args['des'])
    # 循环xml，将所有class放入字典
    for x in xml_list:
        in_file = open(path_annotations + '/' + x)
        tree = et.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            cls_n = obj.find('name').text
            class_name_exists(cls_n)

    # 将classes写入classes文件
    current_path = os.getcwd()
    out_file = open(current_path + '/' + args['des'] + '/' + class_file_name, 'w')
    for cls in class_names:
        out_file.write(cls + '\n')

    # 根据classes的数量，生成对应的cfg文件
    # max_batched: 分类*2000，不少于6000，不少于图片数 $a
    # steps: max_batched 的80%  90% $b  $c
    # $d filter  $e classes
    var_a = len(class_names) * 2000
    if var_a < 6000:
        var_a = 6000
    var_b = int(var_a * 0.8)
    var_c = int(var_a * 0.9)
    var_e = len(class_names)
    var_d = (var_e + 5) * 3

    origin_text = read_file_as_str(args["cfg"])
    st = Template(origin_text)
    new_text = st.safe_substitute({'a': var_a, 'b': var_b, 'c': var_c, 'd': var_d, 'e': var_e})
    out_file_tmp = open(current_path + '/' + args['des'] + '/yolov3.cfg', 'w')
    out_file_tmp.write(new_text)
