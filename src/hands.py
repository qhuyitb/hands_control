import cv2
import mediapipe as mp
import pyautogui

x1 = y1 =0
x2 =y2 =0
# khoi tao webcam
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands() # khoi tao modun nhan dien xong khoi tao class nhan dien tay
drawing_utils = mp.solutions.drawing_utils #ve cac diem ban tay
while True :
    #doc image tu webcam
    _ , image = webcam.read()
    image = cv2.flip(image,1)
    frame_height, frame_width,_ = image.shape # dai X rong
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image) # xu ly anh dau vao de phat hien ban tay
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id ==8: # ngon tro
                    cv2.circle(img = image, center=(x,y), radius = 8, color = (0,255,255), thickness=3)
                    x1 = x
                    y1 = y
                if id ==4: # ngon cai
                    cv2.circle(img = image, center=(x,y), radius = 8, color = (0,0,255), thickness=3)
                    x2 = x
                    y2 = y
        cv2.line(image, (x1,y1), (x2,y2), (0,255,255), 3) # noi hai diem

        # cong thuc (sqrt(x2-x1)^2 +(y2-y1)^2)//4
        distant = (((x2-x1)**2 + (y2-y1)**2)**(0.5))//4
        if distant > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")




    cv2.imshow("Hand volume control using python", image)


    key = cv2.waitKey(10)
    if key == 27: # ma ascii cua ESC
        break
# code bat buoc de giai phong webcam va close window do cv2 open
webcam.release()
cv2.destroyAllWindows()
