import cv2
import numpy as np

def capaCounting(im):
    #im = cv2.imread(image)
    target_size = (350, 500)  #ขนาดจอที่ต้องการ
    
    #ปรับขนาดแสดงผล
    im = cv2.resize(im, target_size)

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

    cv2.imshow('BW', mask_black)
    
    cv2.waitKey()

    return mask_black

#ฟังก์ชันกำหนดพื้นที่ที่จะดีเทค
def ROI(image,top_left_x,top_left_y,bottom_right_x,bottom_right_y):
    #cv2.rectangle( image, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,0,0), 2)

    # Extract the region of interest (ROI)
    roi = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    return roi


def All_COUNT(qr_result):
    img_filename = str(qr_result) + '.jpg'
    im = cv2.imread(img_filename)
    roi1=ROI(im,0,210,125,330)
    roi2=ROI(im,225,8,374,197)
    capaCounting(roi1)
    capaCounting(roi2)
    cv2.imshow('roi1',  roi1)
    cv2.imshow('roi2',  roi2)





if __name__ == '__main__':

    
    camera_id = 0
    delay = 1
    window_name = 'OpenCV QR-Scan'

    qcd = cv2.QRCodeDetector()

    frame= cv2.imread(f"C:/Users/MTL80199/Downloads/GG.png")
    height, width = frame.shape[:2]

    # print("h : " + str(height) + "w : " + str(width))

    # Define ROI Box Dimensions
    top_left_x = 70
    top_left_y = 180
    bottom_right_x = 200
    bottom_right_y = 40

    # Draw rectangular window for our region of interest   
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 2)

    # Extract the region of interest (ROI)
    roi_frame = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(roi_frame)

    if ret_qr:
        for s, p in zip(decoded_info, points):
            if s:
                print(s)
                color = (0, 255, 0)
                #print('lot: '+decoded_info[0])
            else:
                color = (0, 0, 255)
                #print('QR not found')

            p[:, 0] += top_left_x   # Adjust x position based on offset from full image.
            p[:, 1] += bottom_right_y   # Adjust y position based on offset from full image.

            frame = cv2.polylines(frame,[p.astype(int)],True,color ,1)

        # Capture image when QR code is successfully read
        qr_result = decoded_info[0]
        img_filename = str(qr_result) + '.jpg'
        cv2.imwrite(img_filename , frame)  
        All_COUNT(qr_result)

    cv2.imshow(window_name , frame )
    cv2.waitKey()








