import cv2 as cv
import cvlib as cvlib
from cvlib.object_detection import draw_bbox


img = cv.imread('./photos/eq1.png') # 0 might be making it grey scale
resize = cv.resize(img, (1280, 720))
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
print(bbox)
cv.imwrite("./photos/eq1detect.png",output_image)

for item in label:
  if item in labels:
    labels[item] += 1
    pass
  else:
    labels[item] = 1

print(labels)



cv.waitKey(0)
cv.destroyAllWindows()
