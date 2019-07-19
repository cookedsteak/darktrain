# darktrain

This is a tiny script which makes several files for darknet object detection training sets. 

## Use

Prepare your data-sets and follow the training_example directory structure.

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```

## Explication

1. 预训练模型

1. 训练 cfg 文件

1. 训练文件集的目录

1. 验证文件集的目录

1. 文件对应的labels txt

1. 训练主要参数的 xxx.data

1. 表明训练类别的 xx.names

1. 训练集 Annotation 文件夹，以及所有图片的xml文件

1. 训练集图片 JPEGImages 文件夹

## Reference

## TODO

[] 根据names文件自动获取classes类
[] 一击自动开始训练脚本
[] 自动生成data文件