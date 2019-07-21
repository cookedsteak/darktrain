# darktrain

一个准备darknet训练文件的小脚本。

## 用法

请按照实例中的结构组织你的训练文件夹。

一般需要我们准备5样东西。
1. 训练的图片和标签，通常是 Annotations + JPEGImages 两个文件夹放在根目录。
2. 我们要训练的图片中的类别文件，以 classes.names 命名。
3. 我们的 xxx.data 文件，用来描述各个文件夹的位置。
4. 我们调整的 cfg 文件，放在根目录
5. 我们需要训练的预模型，放在根目录或其他目录

然后执行：

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```
