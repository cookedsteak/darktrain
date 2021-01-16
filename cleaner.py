# -*- coding: utf-8 -*-
import cv2
import argparse
import os


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    # 图片所在文件夹
    ap.add_argument("-j", "--images", required=True, help="origin images directory")
    # 所要过滤的图片尺寸
    ap.add_argument("-f","--filter", type=int, default=40, help="image size you want to filter")
    # 标注所在文件夹
    ap.add_argument("-x", "--annotations", required=True, help="origin annotations directory")
    args = vars(ap.parse_args())

    # 图片文件夹下的文件名列表
    args['images'] = args['images'].rstrip('/')
    args['annotations'] = args['annotations'].rstrip('/')
    jpg_list = os.listdir(args['images'])
    # 以图片为主要依据，开始轮询
    for j in jpg_list:
        img = cv2.imread(args['images'] + '/' + j)
        sp = img.shape
        pn = j.split(".")
        pn.pop(-1)
        # 删除小宽度的图片
        if sp[1] <= args['filter']:
            os.remove(args['images'] + '/' + j)
            if os.path.exists(args['annotations'] + '/' + pn[0] + '.xml'):
                os.remove(args['annotations'] + '/' + pn[0] + '.xml')

