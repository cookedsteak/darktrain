# 功能

archive 将制定文件夹中的图片和标注，汇总到一个文件夹并重新命名，防止重复
cleaner 删除小尺寸图片和无效数据集
classify 将所有xml中的分类集中到 my.classes 文件中
prepare 生成所有训练所需要的文件

# 使用

先汇总图片，-d可以是已经有文件的文件夹，不会覆盖，只会重新添加
python3 archive.py -j [path of src images] -x [path of src annotations] -d [destination directory default is final-popo]
python3 cleaner.py -j [a] -x [xml] 清除尺寸较小的图片 
python3 classify.py -x [xml] 准备分类文件
python3 prepare (暂时只能在汇总文件夹的目录执行)

# TODO
1. prepare 同时根据分类数量生成cfg模板文件
2. prepare 添加执行目录参数
3. 自动化执行脚本，用户只需要放入图片