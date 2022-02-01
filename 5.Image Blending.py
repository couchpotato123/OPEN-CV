import cv2 as cv
img1 = cv.imread('img1.jpg')
img2 = cv.imread('img2.jpg')
img1=cv.resize(img1,(500,500))
img2=cv.resize(img2,(500,500))
dst = cv.addWeighted(img1,0.2,img2,0.8,0)
cv.imshow('dst',dst)
k = cv.waitKey(0)
if k == ord("q"):
    cv.imwrite("dst.png", dst)