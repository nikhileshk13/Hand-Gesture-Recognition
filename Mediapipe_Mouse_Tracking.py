import time
import cv2
import numpy as np
import mediapipe_hands
import pyautogui

cT, pT = 0, 0

# Camera frame size
wcam = 1280
hcam = 720

# values for smoothening
px, py = 0, 0
crx, cry = 0, 0
sm = 5

# values for frame reduction
wfR = 300
hfR = 350

cap=cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
wscr, hscr = pyautogui.size()  # pyautogui function to get height and width of the screen
print(wscr, hscr)
detector = mediapipe_hands.hands_module(maxHands=1)
fl = 0  # To check if click is executed only once

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPos(img)

    cv2.rectangle(img, (wfR,10), (wcam-wfR,hcam-hfR), (255,0,255),2)

    if len(lmList) !=0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        # Condition for navigation
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:

            # Converting co-ordinates based on frame reduction values
            x3 = np.interp(x1,(wfR,wcam-wfR),(0,wscr))
            y3 = np.interp(y1,(10,hcam-hfR),(0,hscr))

            # To reduce shaking
            crx = px + (x3-px) / sm
            cry = py + (y3-py) / sm

            # Navigating mouse based on co-ordinates
            pyautogui.moveTo(wscr-crx, cry)
            cv2.circle(img, (x1, y1), 10, (255,0,255), cv2.FILLED)
            px, py = crx, cry
            fl = 0

        # Condition for clicking
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            length, img, params = detector.findDistance(8,12,img)

            # conditions to prevent multiple clicking
            if length > 50:
                fl = 0
            if length < 50:
                if fl == 0:
                    cv2.circle(img, (params[4], params[5]), 10, (0, 0, 255), cv2.FILLED)
                    pyautogui.click()
                    fl = 1

        if cv2.waitKey(1) == 13:
            exit(0)

    cT = time.time()
    fps = 1 / (cT-pT)
    pT = cT
    cv2.putText(img, f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow('image', img)
    cv2.waitKey(1)

