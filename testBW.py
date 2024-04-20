import cv2
import numpy as np

def capaCounting(filename):
    im = cv2.imread(filename)
    target_size = (400, 400)  #ขนาดจอที่ต้องการ
    
    #ปรับขนาดแสดงผล
    im = cv2.resize(im, target_size)

    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    mask_black = cv2.inRange(hsv, (70, 45, 20), (160, 135, 100))

    mask_black = cv2.medianBlur(mask_black, 5)
    # mask_black = cv2.erode(mask_black, circle_kernel_Y1, iterations=1)
    # mask_black = cv2.dilate(mask_black, circle_kernel_Y2, iterations=1)

    

    # kernel_size_B1 = 15
    # kernel_size_B3 = 11
    # kernel_size_B4 = 2
    # circle_kernel_B1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size_B1, kernel_size_B1))
    # rectangular_kernel_B2 = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size_B3, kernel_size_B4))

    # mask_black = cv2.erode(mask_black, circle_kernel_B1, iterations=1)

    contours_black, hierarchy_yellow = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # #สร้าง array
    # dilation_mask = np.zeros_like(mask_black)

    # #ถ้าเจอจุดเล็กให้ Dilation 
    # for contour in contours_black:
    #     area = cv2.contourArea(contour)
    #     if area < 150:  # Adjust the threshold as needed
    #         # Create a circular kernel for dilation
    #         dilation_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    #         # Dilate only in the region of small contours
    #         dilation_mask = cv2.drawContours(dilation_mask, [contour], 0, 255, -1)
    #         dilation_mask = cv2.dilate(dilation_mask, dilation_kernel, iterations=1)
      
    # #dilation_mask = cv2.erode(mask_blue, rectangular_kernel_B2, iterations=1)
    # #หาใหม่อีกรอบ
    # mask_black = cv2.bitwise_or(mask_black, dilation_mask)
    # mask_black = cv2.erode(mask_black,  rectangular_kernel_B2, iterations=1)
    # contours_black, hierarchy_blue = cv2.findContours(mask_black, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    
    # mask_black = cv2.erode(mask_black, circle_kernel_B1, iterations=1)
    

    

    black = len(contours_black)

    print('CAPCount :',black)

    cv2.imshow('Original Image', im)
    cv2.imshow('BW', mask_black)
    
    cv2.waitKey()

    return black

capaCounting('C:/Users/MTL80199/Pictures/Screenshots/capa3.png')