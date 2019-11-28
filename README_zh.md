# darktrain

一个准备darknet训练文件的小工具。

## 用法

请按照实例中的结构组织你的训练文件夹。

我们准备4样东西。
1. 训练的图片和标签，通常是 Annotations + JPEGImages/JPEGImages_val 两个文件夹放在根目录。
2. 我们要训练的图片中的类别文件，以 classes.names 命名。
4. 我们调整的 cfg 文件，放在根目录
5. 我们需要训练的预模型，放在根目录或其他目录

其余的辅助文件，prepare.py 脚本都会自动生成。

* JPEGImages_val是验证图片文件夹，如果没有验证图片，可以将训练图片复制进验证文件夹

准备好需要的文件，然后执行：

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```

然后利用
```bash
./darknet detector train [data文件] [cfg文件] [预训练模型] -clear 1 (如果使用预训练模型)
```
进行训练 :)

测试可以使用如下命令
```bash
./darknet detector test [data] [cfg] [weights] [jpeg] -thresh 0.1
```

## 参考

关于darknet训练的详细教程，可以参考[这里](https://github.com/AlexeyAB/darknet)

## TODO

设置是否需要验证集文件夹的flag