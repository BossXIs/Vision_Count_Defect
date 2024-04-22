import cv2
import numpy as np

def capaCounting(image):
    target_size = (400, 400)  # ขนาดจอที่ต้องการ
    
    # ปรับขนาดแสดงผล
    im = cv2.resize(image, target_size)

    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    mask_black = cv2.inRange(hsv, (70, 45, 20), (160, 135, 100))

    mask_black = cv2.medianBlur(mask_black, 5)
   
    contours_black, hierarchy_yellow = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # นับจำนวนอ็อบเจ็กต์ทั้งหมด
    black = len(contours_black)

    print('CAPCount :', black)

    return black, im, mask_black

def divide_and_count_objects(filename):
    im = cv2.imread(filename)
    target_size = (400, 400)  # ขนาดจอที่ต้องการ
    
    # ปรับขนาดแสดงผล
    im = cv2.resize(im, target_size)

    # แบ่งภาพออกเป็น 9 ช่อง
    sub_images = []
    rows, cols, _ = im.shape
    cell_width = cols // 3
    cell_height = rows // 3

    for y in range(3):
        for x in range(3):
            sub_img = im[y * cell_height:(y + 1) * cell_height, x * cell_width:(x + 1) * cell_width]
            sub_images.append(sub_img)

    # นับจำนวนอ็อบเจ็กต์ในแต่ละช่อง
    for i, sub_img in enumerate(sub_images):
        count, original_img, bw_img = capaCounting(sub_img)
        cv2.imshow(f'Cell {i + 1}: Objects Count: {count}', np.hstack((original_img, cv2.cvtColor(bw_img, cv2.COLOR_GRAY2BGR))))

    cv2.waitKey()

# เรียกใช้งานฟังก์ชัน divide_and_count_objects
divide_and_count_objects("C:/Users/MTL80199/Pictures/Screenshots/capa4.png")