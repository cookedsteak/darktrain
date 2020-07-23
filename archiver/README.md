# 功能

archive 将制定文件夹中的图片和标注，汇总到一个文件夹并重新命名，防止重复
cleaner 删除小尺寸图片和无效数据集
classify 将所有xml中的分类集中到 my.classes 文件中

# 使用

python3 archive.py -j [path of src images] -x [path of src annotations] -d [destination directory default is final-popo]