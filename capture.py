import cv2
print(cv2.__version__)
cap = cv2.VideoCapture(0)
ret,im = cap.read()
im_flipped = cv2.flip(im,1)
cv2.imshow('camera',im_flipped)
cv2.waitKey()
cap.release()