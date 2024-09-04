import cv2 as cv
import cvlib as cvlib
from cvlib.object_detection import draw_bbox
import time

def videoOutput(frame):
  img = cv.imread(frame)
  resize = cv.resize(img, (800, 600))
  labels = {}
  #equalized_image = cv.equalizeHist(resize) #grey scale image (i think)

  # binary image
  #threshold_value = 127
  #maximum_value = 255
  #_, binary_image = cv.threshold(equalized_image, threshold_value, maximum_value, cv.THRESH_BINARY)
  #cv.imshow('test', binary_image)

  #adaptive thresholding
  # maximum_value = 255
  # adaptive_method = cv.ADAPTIVE_THRESH_MEAN_C
  # threshold_type = cv.THRESH_BINARY
  # block_size = 11
  # constant = 2
  # binary_image = cv.adaptiveThreshold(equalized_image, maximum_value, adaptive_method, threshold_type, block_size, constant)
  # cv.imshow('test', binary_image)

  #guassian blur
  # ksize = (5, 5)
  # sigma = 0
  # blurred_image = cv.GaussianBlur(equalized_image, ksize, sigma)
  # cv.imshow('test', resize)

  #canny edge detection, algorithm for detecting edges
  # threshold1 = 125 # min val
  # threshold2 = 175 # max val
  # edges = cv.Canny(resize, threshold1, threshold2)

  # contours, hierarchies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
  # cv.imshow('test', img)


  bbox, label, conf = cvlib.detect_common_objects(resize)
  output_image = draw_bbox(resize, bbox, label, conf)

  cv.imshow("Object Detection", output_image)

  # for item in label:
  #   if item in labels:
  #     labels[item] += 1
  #     pass
  #   else:
  #     labels[item] = 1

  time.sleep(1)
  # cv.waitKey(0)
  # cv.destroyAllWindows()
  return bbox


# This is an example of how the drone takes pictures and analyzes them
# Importing dependencies
import cv2 as cv
import cvlib as cvlib
from cvlib.object_detection import draw_bbox
import time
from djitellopy import Tello

# Setup Tello drone
tello = Tello()
tello.connect()
tello.streamon()

# Read the frame (take picture)
frame_read = tello.get_frame_read()
time.sleep(1)

# Write the picture to picture.png
cv.imwrite("picture.png", frame_read.frame)

# Read that picture and resize it
img = cv.imread('picture.png')
resize = cv.resize(img, (800, 600))

# Using the cv common object detection library, it is able to detect common objects in the picture
# Bbox are the coordinates of where the detection was made
# Label is the label that the object was determined to be
# Conf is the confidence level
bbox, label, conf = cvlib.detect_common_objects(resize)
output_image = draw_bbox(resize, bbox, label, conf)

# Now show the image
cv.imshow("Object Detection", output_image)

# With the image captures the and image analyzed, we can now interpret the image and decide what the
# drone should do next. 
