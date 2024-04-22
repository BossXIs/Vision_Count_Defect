import cv2
import numpy as np

def capaCounting(image):
    im = cv2.imread(image)
    #target_size = (400, 400)  #ขนาดจอที่ต้องการ
    
    #ปรับขนาดแสดงผล
    #im = cv2.resize(im, target_size)

    #เปลี่ยน BGR --> HSV
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    #ปรับ Threshold สีที่ต้องการ
    mask_black = cv2.inRange(hsv, (70, 45, 20), (160, 135, 100))

    #เบลอภาพ
    mask_black = cv2.medianBlur(mask_black, 5)

    #นับจำนวน
    contours_black, hierarchy_yellow = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    black = len(contours_black)

    #ROI(im,70,180,200,40)

    print('CAPCount :',black)

    #cv2.imshow('BW', mask_black)
    
    #cv2.waitKey()

    return mask_black

#ฟังก์ชันกำหนดพื้นที่ที่จะดีเทค
def ROI(image,top_left_x,top_left_y,bottom_right_x,bottom_right_y):
    #cv2.rectangle(image, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,0,0), 2)

    # Extract the region of interest (ROI)
    roi = image[top_left_y:bottom_right_y , top_left_x:bottom_right_x]

    return roi

###################main########################
im = cv2.imread("C:/Users/MTL80199/Downloads/GG.png")
roi_qr=ROI(im,70,40,200,180)
roi1=ROI(im,0,210,125,330)
roi2=ROI(im,225,8,374,197)
#roi3=ROI(im,0,150,200,40)
#roi4=ROI(im,0,120,700,40)
#count=capaCounting(im)
cv2.imshow('QR',roi_qr)
cv2.imshow('roi1',roi1)
#cv2.imshow('count',count)
cv2.imshow('roi2',roi2)
#cv2.imshow('roi3',roi3)
#cv2.imshow('roi4',roi4)
cv2.waitKey()








