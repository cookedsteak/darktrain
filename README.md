# darktrain

This is a tiny script which prepare several files for darknet object detection training sets.
[中文版]()说明请看这里

## Use

Prepare your data-sets and follow the training_example directory structure.

## Preparation

Please according to the structure of the example directory.

Normally, we need 5 things in our training directory.

1. Annotations + JPEGImages
2. classes.names
3. xxxx.data
4. cfg
5. pre-trained model

Once we have these things above, run:

```bash
$ cd [your/data-set/directory]
$ python3 prepare.py
```

Then you will get all txt files/ labels in your directory.


