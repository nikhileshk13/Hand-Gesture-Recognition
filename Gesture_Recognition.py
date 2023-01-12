from tensorflow.keras.models import load_model
import mediapipe_hands
import cv2
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def gesname(val):
    if val == 0:
        return 'back'
    elif val==1:
        return 'forward'
    elif val==2:
        return 'submit'
    else:
        return 'exit/end'


classifier = load_model('CNN_model.h5')
detector = mediapipe_hands.hands_module(maxHands=1)
cap = cv2.VideoCapture(0)


while True:
    try:
        success, img = cap.read()

        # Obtaining the bounding box for hand from mediapipe module
        img = detector.findHands(img, draw=False)
        lmList, bbox = detector.findPos(img, draw=False)
        roi = img.copy()
        if len(bbox) != 0:
            # Cropping the image to the size of bounding box
            roi = img[bbox[1] - 15:bbox[3] + 15, bbox[0] - 15:bbox[2] + 15]

            # Resizing the image to input size of the model and rescaling
            roi = cv2.resize(roi, (75, 75), interpolation=cv2.INTER_AREA)
            roi = roi.reshape(1, 75, 75, 3)
            roi = roi / 255

            # Prediction using the CNN Model
            result = np.argmax(classifier.predict(roi, verbose=0) > 0.7, axis=1)
            result2 = gesname(result)
            cv2.putText(img, str(result2), (300, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

        if cv2.waitKey(1) == 13:
            exit(0)

    except Exception as e:
        cv2.putText(img, 'Out of focus', (30, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow('frame', img)


cap.release()
cv2.destroyAllWindows()

