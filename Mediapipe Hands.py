import cv2
import mediapipe as mp
import time
import math


class hands_module():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        # object of hands module in mediapipe
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        # mediapipe method to draw points on hands
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        # hands class takes rgb image so we have to convert it to rgb
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # method of hands class that will process the frame and give the result
        self.results = self.hands.process(imgRGB)

        # checking the number of hands detected and drawing landmark points for each hand
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # drawing the connections
        return img


    def findPos(self, img, handNo=0, draw=True):
        # create list to store landmark values
        self.lmList = []
        xl = []
        yl = []
        bbox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo] #access landmark values based on handno
            # get id number and landmark information(x,y) coordinate for each landmark
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                # convert integer x,y values of landmarks into pixel values
                cx, cy = int(lm.x * w), int(lm.y * h)
                xl.append(cx)
                yl.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    # drawing circle around the landmarks
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

            # create bounding box to reduce resolution to make it smoother
            xmin, xmax = min(xl), max(xl)
            ymin, ymax = min(yl), max(yl)
            bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(img,(bbox[0]-20,bbox[1]-20),(bbox[2]+20,bbox[3]+20),(0,255,0),2)
        return self.lmList, bbox


    def fingersUp(self):
        fingers = [0]
        for tid in range(8, 21, 4):
            # condition for forefingers
            if self.lmList[tid][2] < self.lmList[tid - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
            # condition for thumb
            if self.lmList[4][1] > self.lmList[3][1]:
                fingers[0] = 1
            else:
                fingers[0] = 0

        return fingers


    def findDistance(self,p1,p2,img,draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        if draw:
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        length = math.hypot((x2 - x1), (y2 - y1))
        return length,img,[x1,y1,x2,y2,cx,cy]


def main():
    pT = 0
    cT = 0
    cap = cv2.VideoCapture(0)
    detector = hands_module()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPos(img)
        if len(lmList) != 0:
            print(lmList[8])
        cT = time.time()
        fps = 1 / (cT - pT)
        pT = cT
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)

        cv2.imshow('image', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
