import cv2
import mediapipe as mp
import numpy as np
mscam = 10
tomato = []
for i in range(mscam):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        tomato.append(i)

cc = cv2.VideoCapture(tomato[0])
mphand = mp.solutions.hands
handc = mphand.Hands()
cc_blank = 1920
cr_blank = 1080
cc_cam = 500
cr_cam = 800
cc_logo = 120
cr_logo = 120

while True:
    img = cv2.imread('vcvt.png')
    sc , fr = cc.read()

    frame_resize = cv2.resize(fr,(cc_cam,cr_cam ))
    img_resize = cv2.resize(img,(cc_logo,cr_logo))
    blank = np.ones((cr_blank,cc_blank,3),dtype = 'uint8')*255
    x_set = 0
    y_set = 0
    x_set2 =  cc_blank - cc_logo -10
    y_set2 = cr_blank - cr_logo - 10
    blank[y_set:y_set+cr_cam , x_set:x_set+cc_cam]=frame_resize
    blank[y_set2:y_set2 + cr_logo, x_set2:x_set2 + cc_logo] = img_resize
    cv2.rectangle(blank, (x_set2, y_set2), (x_set2 + cc_logo, y_set2 + cr_logo), (0, 255, 0), 2)

    imrgb = cv2.cvtColor(blank, cv2.COLOR_BGR2RGB)
    re = handc.process(imrgb)
    if re.multi_hand_landmarks:

        for hlm in re.multi_hand_landmarks:
         xl = []
         yl = []
         xl1 , yl1 = 0,0
         xl2 ,yl2 = 0,0


         h,w,c = blank.shape

         for i , hlm in enumerate(re.multi_hand_landmarks):
            for id, lm in enumerate(hlm.landmark):
             if id == 9:
                cx , cy = int(lm.x*w),int(lm.y*h)
                xl.append(cx)
                yl.append(cy)
                if i == 0:
                  xl1 =cx
                  yl1=cy
                  cv2.circle(blank, (xl1, yl1), 2, (0, 0, 255), 20)
                  cv2.circle(blank, (xl1, yl1), 60, (0, 0, 255), 20)
                  cv2.line(blank, (xl1, 0), (xl1, yl1), (0, 0, 0), 3)
                  cv2.line(blank, (0, yl1), (xl1, yl1), (0, 0, 0), 3)
                  cv2.line(blank, (500, yl1), (xl1, yl1), (0, 0, 0), 3)
                  cv2.line(blank, (xl1, 800), (xl1, yl1), (0, 0, 0), 3)
                  cv2.putText(blank, f"{xl1}mm ,{yl1}mm", (xl1, yl1 - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2,
                              cv2.LINE_AA)

                elif i == 1:
                  xl2= cx
                  yl2=cy
                  cv2.circle(blank, (xl2, yl2), 2, (0, 0, 255), 20)
                  cv2.circle(blank, (xl2, yl2), 60, (0, 0, 255), 20)
                  cv2.line(blank, (xl2, 0), (xl2, yl2), (0, 0, 0), 3)
                  cv2.line(blank, (0, yl2), (xl2, yl2), (0, 0, 0), 3)
                  cv2.line(blank, (500, yl2), (xl2, yl2), (0, 0, 0), 3)
                  cv2.line(blank, (xl2, 800), (xl2, yl2), (0, 0, 0), 3)
                  cv2.putText(blank, f"{xl2}mm ,{yl2}mm", (xl2, yl2 - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2,
                              cv2.LINE_AA)


                cv2.putText(blank, f"so tay: {len(re.multi_hand_landmarks)}", (600,50), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 6,
                            cv2.LINE_AA)


         cv2.putText(blank, f"toa do tay 1:({xl1},{yl1})", (600, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
                            6,
                            cv2.LINE_AA)
         cv2.putText(blank, f"toa do tay 2:({xl2},{yl2})", (600, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
                            6,
                            cv2.LINE_AA)

    else:
        cv2.putText(blank, "so tay: 0", (600, 50), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 6,
                    cv2.LINE_AA)
        cv2.putText(blank, f"toa do tay 1:(0,0)", (600, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
                    6,
                    cv2.LINE_AA)
        cv2.putText(blank, f"toa do tay 2:(0,0)", (600, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0),
                    6,
                    cv2.LINE_AA)

    cv2.imshow("cam",blank)
    cv2.waitKey(1)