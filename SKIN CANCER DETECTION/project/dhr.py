import cv2
 
src = cv2.imread("/media/anandhkrishna/asgard/test/587.jpg")
print( src.shape )
grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
kernel = cv2.getStructuringElement(1,(17,17))
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
ret, thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
cv2.imwrite("/media/anandhkrishna/asgard/test/587_hair_remove.jpg", dst, [int(cv2.IMWRITE_JPEG_QUALITY), 100])