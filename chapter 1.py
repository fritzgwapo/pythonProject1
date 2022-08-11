# ####################### READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Videos/IMG_20220111_190142_1.jpg")
# frameWidth = 120
# frameHeight = 60
# cv2.imshow("samples",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
import cv2
frameWidth = 400
frameHeight = 200
cap = cv2.VideoCapture("Videos/video_20220111_184625.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
######################### READ WEBCAM  ############################
# import cv2
# frameWidth = 640
# frameHeight = 480
# source = cv2.VideoCapture(0)
# source.set(3, frameWidth)
# source.set(4, frameHeight)
# source.set(10,10)
# while True:
#     success, img = source.read()
#     gray = cv2.cvtColor(img,COLOR_BGR2GRAY)
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break