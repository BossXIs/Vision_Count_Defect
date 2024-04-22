import cv2 
import numpy as np 
  
# Read image 
image = cv2.imread("C:/Users/MTL80199/Downloads/GG.png") 
  
# Select ROI 
r = cv2.selectROI("select the area", image) 
  
# Crop image 
cropped_image = image[int(r[1]):int(r[1]+r[3]),  
                      int(r[0]):int(r[0]+r[2])] 

# Get x, y coordinates of cropped_image
x = int(r[0])
y = int(r[1])

start_x = int(r[0])
start_y = int(r[1])

# Get x,y coordinates of bottom-right corner of cropped_image
end_x = start_x + int(r[2])  # Adding width to x coordinate
end_y = start_y + int(r[3])  # Adding height to y coordinate

print(f"Start Coordinates: ({start_x}, {start_y})")
print(f"End Coordinates: ({end_x}, {end_y})")

# Display cropped image 
cv2.imshow("Cropped image", cropped_image) 
cv2.waitKey(0)

print("Coordinates (x, y):", x, y)