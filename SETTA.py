import cv2
import obj_count

camera_id = 0
delay = 1
window_name = 'OpenCV QR-Scan'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
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
                else:
                    color = (0, 0, 255)

                p[:, 0] += top_left_x   # Adjust x position based on offset from full image.
                p[:, 1] += bottom_right_y   # Adjust y position based on offset from full image.

                frame = cv2.polylines(frame,[p.astype(int)],True,color ,1)

            # Capture image when QR code is successfully read
            qr_result = decoded_info[0]
            img_filename = str(qr_result) + '.jpg'
            cv2.imwrite(img_filename , frame)  
            obj_count.obj_count_main(qr_result)

        cv2.imshow(window_name , frame )

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name )