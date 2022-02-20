# Image Recognition

A command line program based on [ImageAi](https://github.com/OlafenwaMoses/ImageAI) python library that can recognize images and return the it's predicted name with the probability of it's correctness and can also detect the objects in the image.

## Dependencies

You must have installed following packages:

1. ImageAi 2.1.6
1. Tensorflow 2.4.0
1. OpenCV 4.5.5.62
1. Keras 2.4.3

### Other dependencies

```
h5py==2.10.0 matplotlib==3.3.2 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1
```

## Installation

- Clone the repository
- Go to the directory
- Run the following command:

```
pip install -r requirements.txt
```

Note: Tensorflow 2.4.0 is compatible with only Python<=3.7.6 and you might need to create a virtual environment for your python version if you are on upper version.

## Usage

    usage: main.py [-h] -i IMAGE [-o OUTPUT] [-p PREDICT] [-d DETECT]

    optional arguments:
    -h, --help            show this help message and exit
    -i IMAGE, --image IMAGE
                            path to Image file
    -o OUTPUT, --output OUTPUT
                            path to Output file
    -p PREDICT, --predict PREDICT
                            use this argument when want to make prediction about
                            the image
    -d DETECT, --detect DETECT
                            use this argument when want to detect objects in the
                            image

Examples:

Prediction of an image:

    > python src/main.py -i assets/images/car.jpg -p

    convertible  :  41.79445207118988
    beach_wagon  :  15.723656117916107
    sports_car  :  14.756788313388824
    car_wheel  :  13.611182570457458
    grille  :  1.7730096355080605

Detect objects in an image:

    > python src/main.py -i assets/images/family.jpg -o assets/images/family-detected.jpg -d

    person  :  56.48157000541687  :  [160, 95, 294, 322]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/person-1.jpg
    --------------------------------
    person  :  83.2624077796936  :  [290, 177, 400, 273]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/person-2.jpg
    --------------------------------
    person  :  52.868008613586426  :  [404, 126, 572, 309]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/person-3.jpg
    --------------------------------
    laptop  :  33.79327952861786  :  [286, 252, 407, 299]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/laptop-4.jpg
    --------------------------------
    donut  :  54.71799373626709  :  [0, 378, 155, 442]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/donut-5.jpg
    --------------------------------
    donut  :  33.92322063446045  :  [33, 371, 115, 451]
    Object's image saved in /home/hemant/Projects/ImageRecognition/assets/images/family-detected.jpg-objects/donut-6.jpg
    --------------------------------

## More Information

Github do not allow uploading files with a size greater than 100MB. So all the examples and used training models are smaller in size but there are more models that can be used for prediction and detection with more accuracy.

Prediction models:

1. [ResNet50](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_imagenet_tf.2.0.h5) by Microsoft Research (Size = 98 mb, fast prediction time and high accuracy)

1. [InceptionV3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5) by Google Brain team (Size = 91.6 mb, slow prediction time and higher accuracy)

1. [DenseNet121](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5) by Facebook AI Research (Size = 31.6 mb, slower prediction time and highest accuracy)

Object detection models:

1. [RetinaNet](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5) (Size = 145 mb, high performance and accuracy, with longer detection time)

1. [YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5) (Size = 237 mb, moderate performance and accuracy, with a moderate detection time)
