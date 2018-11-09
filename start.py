import cv2
from keras.applications.resnet50 import ResNet50
import numpy
X = numpy.array()


vidcap = cv2.VideoCapture('testing/test_3.mov')
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("testing/test_3/test_3_frame_%d.jpg" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success, count)
    count += 1
