# 准备

利用工具生成的图片和xml标注文件。

# 功能

将图片和标注转化为可以训练的文件结构。

### archive.py
`python archive.py -j [源图片文件夹] -x [源标注文件夹] -d [整理后的新文件夹]`
 
将制定文件夹中的图片和标注，汇总到一个文件夹并重新命名，防止重复。


### cleaner.py 
`python cleaner.py -j [图片文件夹] -x [标注文件夹]`

删除小尺寸图片和无效关联图片，同时删除对应标注文件。

### classify.py
`python classify.py -x [标注文件位置] -d [存放分类和配置文件的位置]`
 
将所有xml中的分类集中到 my.classes 文件中，并且自动生成训练配置cfg文件。

### prepare.py
`python prepare.py -d [目标文件夹]`
 
生成所有训练所需要的标签、位置文件。

### darktrain.sh 
`./darktrain [源图片文件夹] [源标注文件夹]`

整合在一起的bash脚本。
默认生成xxx_after文件夹存放处理后的数据。

# 训练
`./darknet detector train cfg/coco.data yolov4.cfg yolov4.conv.137`

# TODO
1. [x] prepare 同时根据分类数量生成cfg模板文件
2. [x] 自动化执行脚本，用户只需要放入图片和标注