# darktrain
training tool for darknet

## Use

准备数据集目录，参照 example。
执行 prepare.py

```python
python3 prepare.py
```

## 必要的文件

1. 预训练模型

1. 训练 cfg 文件

1. 训练文件集的目录

1. 验证文件集的目录

1. 文件对应的labels txt

1. 训练主要参数的 xxx.data

1. 表明训练类别的 xx.names

1. 训练集 Annotation 文件夹，以及所有图片的xml文件

1. 训练集图片 JPEGImages 文件夹