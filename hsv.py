import numpy as np
import cv2
TARGET_SIZE = (640, 360)
for i in range(1, 33):
   im = cv2.imread(f"C:/Users/MTL80199/Pictures/Screenshots/black/black{i}.png")
   im_resized = cv2.resize(im, TARGET_SIZE)
   im_flipped = cv2.flip(im_resized, 1)
   mask = cv2.inRange(im_flipped, (0, 0, 90), (50, 50, 255))
   #############################################
   h, w = im_flipped.shape[:2]
   im_cropped = im_flipped[(int(h/2)-8):(int(h/2)+9),
                           (int(w/2)-8):(int(w/2)+9),
                           :]
   # Convert the cropped region to HSV
   im_cropped_hsv = cv2.cvtColor(im_cropped, cv2.COLOR_BGR2HSV)
   cv2.imshow('cropped', cv2.resize(im_cropped, (128, 128)))
   cv2.moveWindow('cropped', 0, TARGET_SIZE[1])
   b = int(np.mean(im_cropped[:, :, 0]))
   g = int(np.mean(im_cropped[:, :, 1]))
   r = int(np.mean(im_cropped[:, :, 2]))
   cv2.rectangle(im_flipped,
                 (int(w/2)-8, int(h/2)-8),
                 (int(w/2)+8, int(h/2)+8),
                 (255, 255, 255))
   cv2.putText(im_flipped, str(b), (20, 30),
               cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
   cv2.putText(im_flipped, str(g), (90, 30),
               cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
   cv2.putText(im_flipped, str(r), (160, 30),
               cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
   # Print HSV values
   h_mean = int(np.mean(im_cropped_hsv[:, :, 0]))
   s_mean = int(np.mean(im_cropped_hsv[:, :, 1]))
   v_mean = int(np.mean(im_cropped_hsv[:, :, 2]))
   print(f"HSV{i}: {h_mean} {s_mean} {v_mean}")
cv2.destroyAllWindows()