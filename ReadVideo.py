import cv2 as cv
cap=cv.VideoCapture(0)                     #you can input 0,1,2 according to the list of webcams and you can use any video file also
while True:
    ret,frame=cap.read()
    cv.imshow('Frame',frame)
    if cv.waitKey(1) &0xFF==ord('e') :
        break
cap.release()
cv.destroyAllWindows()
