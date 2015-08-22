import cv2
# import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())

# image = cv2.imread(args["image"])
image = cv2.imread("C:\\Ragha\github\\ImageProcessingUsingPythonOpencv\\images\\rafting.jpg")
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d" % (image.shape[2])

cv2.imshow("Image", image)
cv2.imwrite("newimage.bmp", image)
cv2.waitKey(0)
