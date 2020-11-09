import cv2
img = cv2.imread("file.jpg",-1)                   #add your file name
print(img)

cv2.imshow("Image", img)

cv2.waitKey()

cv2.destroyAllWindows()
