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

#cv2.imshow("Image", image)
#cv2.imwrite("newimage.bmp", image)

#get pixel 
#(b, g, r) = image[0, 0]
#print "Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b)

#set pixel
#image[0, 0] = (0, 0, 255)
#(b, g, r) = image[0, 0]
#print "Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b)

#grab a portion of image

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:50, 0:100] = (0, 255, 0)#first parameter is y, second is x!
cv2.imshow("Updated", image)

#cv2.imshow("Image", image)
cv2.waitKey(0)
