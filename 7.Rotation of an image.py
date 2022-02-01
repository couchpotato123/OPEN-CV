import cv2 as cv
img = cv.imread("img3.jpg",0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('dst',dst)
k = cv.waitKey(0)
if k == ord("q"):
    cv.imwrite("dst.png", dst)