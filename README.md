# darktrain

This is a tiny script which prepare several files for darknet object detection training sets.

[中文版](https://github.com/cookedsteak/darktrain/blob/master/README_zh.md)说明请看这里


## What for

Automatically generates necessary files for training darknet models such as:

- label files
- .data file
- image list
- annotation list

## Use

1. Get ready for your data-sets(Annotations + JPEGImages) and place them following the structure of `training_example` directory.

2. Make your own `classes` file and name it as `classes.names`.

3. Copy a `.cfg` file and adjust some parameters.
 
5. Prepare a pre-trained model(darknet53.cnv.74).

Once we finished our preparation:

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```

Necessary files will be generated automatically in your training directory.

Then use command `./darknet detector train [data-file path] [cfg-file path] [pre-trained model path]` to train your own model :)


## Reference

- https://github.com/AlexeyAB/darknet


## TODO

1. Automatic `.cfg` file generator