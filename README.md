# darktrain

This is a tiny script which prepare several files for darknet object detection training sets.

[中文版](https://github.com/cookedsteak/darktrain/blob/master/README_zh.md)说明请看这里

## Use

Prepare your data-sets and follow the training_example directory structure.

## Preparation

Please according to the structure of the example directory.

Normally, you need 4 things prepared in our training directory.

1. Annotations + JPEGImages
2. classes.names
4. cfg
5. pre-trained model

Once we have these things above, run:

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```

Other files will be generated automatically in your training directory.

Then use `./darknet detector train` to train your own model.

